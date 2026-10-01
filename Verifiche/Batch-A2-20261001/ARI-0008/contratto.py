from pathlib import Path
def percorso_autorizzato(base, nome):
    target=(Path(base)/nome).resolve()
    if not target.is_relative_to(Path(base).resolve()):
        raise ValueError('Fuori perimetro')
    return target
