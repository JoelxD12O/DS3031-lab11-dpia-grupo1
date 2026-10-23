# Lab 11 · Backend mínimo + DPIA (DS3031)

Backend de registro (nombres, apellidos, correo y teléfono) **sin protecciones de privacidad, a propósito**. Sus problemas son el objeto de la DPIA (`DPIA_Grupo.docx`). Lo único no negociable, y que sí se aplica, son las consultas parametrizadas.

## Contenido

| Archivo | Qué es |
|---|---|
| `app.py` | API Flask + SQLite: `POST /registro`, `GET /registros`, `GET /` (formulario) |
| `static/index.html` | Front opcional: formulario + tabla con la respuesta de `GET /registros` |
| `DPIA_Grupo.docx` | DPIA en la plantilla ICO del curso: descripción, inventario, necesidad, 10 riesgos (LINDDUN), medidas C-01 a C-10, riesgo residual y decisión |
| `CHECKLIST.md` | IntroPrivacy Checklist del curso, con la columna "Componente por crear" |

## Ejecutar

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows  (Linux/Mac: source .venv/bin/activate)
pip install -r requirements.txt
flask --app app run
```

Abrir http://localhost:5000 para usar el formulario.

## Probar con curl (personas inventadas)

```bash
curl -X POST localhost:5000/registro -H "Content-Type: application/json" \
  -d '{"nombres":"Ana","apellidos":"Quispe","correo":"ana@correo.pe","telefono":"+51 987 654 321"}'

curl localhost:5000/registros
```

> `lab.db` se crea al arrancar y **no se sube al repositorio** (ver `.gitignore`).
