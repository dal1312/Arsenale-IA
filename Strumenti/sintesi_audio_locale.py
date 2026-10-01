"""Adattatore Piper/Kokoro: usa solo modelli esplicitamente indicati e locali."""
from __future__ import annotations

import argparse
import io
import re
import wave
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--engine', choices=('piper', 'kokoro'), required=True)
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--model', type=Path, required=True)
    parser.add_argument('--voices', type=Path)
    parser.add_argument('--voice', required=True)
    parser.add_argument('--speed', type=float, default=0.95)
    args = parser.parse_args()
    text = args.input.read_text(encoding='utf-8-sig').strip()
    if not text or not args.model.is_file() or not 0.5 <= args.speed <= 2:
        parser.error('Testo, modello o velocità non validi')
    if args.output.exists():
        parser.error('Output già presente')
    parts = re.findall(r'\S+(?:\s+\S+){0,49}', text)
    chunks = []
    import numpy as np

    if args.engine == 'piper':
        from piper import PiperVoice, SynthesisConfig
        if args.voice != 'paola':
            parser.error('Voce Piper non configurata')
        voice = PiperVoice.load(str(args.model), use_cuda=False)
        for part in parts:
            buffer = io.BytesIO()
            with wave.open(buffer, 'wb') as wav:
                voice.synthesize_wav(part, wav, syn_config=SynthesisConfig(
                    volume=0.85, length_scale=1 / args.speed))
            buffer.seek(0)
            with wave.open(buffer, 'rb') as wav:
                rate = wav.getframerate()
                if wav.getnchannels() != 1 or wav.getsampwidth() != 2:
                    raise RuntimeError('Formato Piper inatteso')
                samples = np.frombuffer(wav.readframes(wav.getnframes()), dtype='<i2')
                chunks.append(samples.astype(np.float32) / 32768)
    else:
        from kokoro_onnx import Kokoro
        if args.voices is None or not args.voices.is_file():
            parser.error('Pacchetto voci assente')
        voice = Kokoro(str(args.model), str(args.voices))
        if args.voice not in ('im_nicola', 'if_sara') or args.voice not in voice.get_voices():
            parser.error('Voce italiana non disponibile')
        for part in parts:
            samples, rate = voice.create(part, voice=args.voice, lang='it', speed=args.speed)
            chunks.append(samples)

    samples = np.concatenate([chunk for part in zip(chunks, [np.zeros(int(rate * 0.15))] * len(chunks))
                              for chunk in part][:-1])
    if not len(samples) or not np.isfinite(samples).all():
        raise RuntimeError('Campioni assenti o non finiti')
    peak = float(np.max(np.abs(samples)))
    if peak == 0:
        raise RuntimeError('Audio silenzioso')
    if peak > 0.89:
        samples = samples * (0.89 / peak)
    frames = (samples * 32767).astype('<i2').tobytes()
    with args.output.open('xb') as output:
        with wave.open(output, 'wb') as wav:
            wav.setnchannels(1)
            wav.setsampwidth(2)
            wav.setframerate(rate)
            wav.writeframes(frames)


if __name__ == '__main__':
    main()
