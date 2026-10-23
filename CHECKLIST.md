# IntroPrivacy Checklist — estado del backend mínimo

Columna **Estado hoy**: lo que cumple el backend entregado. El backend no tiene protecciones a propósito: es el objeto de la DPIA.
Columna **Componente por crear**: la medida (C-xx) del Step 6 de `DPIA_Grupo.docx` que lo resuelve.

| # | Ítem | Estado hoy | Componente por crear |
|---|---|---|---|
| **Consentimiento y recopilación de datos** | | | |
| 4 | Mecanismo claro para obtener el consentimiento antes de recopilar | ☐ | C-04: casilla por finalidad, desmarcada + tabla `consentimiento` (finalidad, versión, fecha, retiro) |
| 5 | El formulario especifica para qué se usarán los datos | ☐ | C-04: aviso de capa 1 junto al botón |
| 6 | Evitar recopilar datos innecesarios | ☐ | C-03: eliminar `telefono`; `apellidos` opcional |
| **Acceso y control sobre los datos personales** | | | |
| 8 | Interfaz para que el usuario acceda a sus datos | ☐ | C-06: `GET /me` + vista *Mi cuenta* |
| 9 | Editar o corregir sus datos | ☐ | C-06: `PATCH /me`, que deja rastro en auditoría (C-09) |
| 10 | Eliminar la cuenta y todos sus datos | ☐ | C-06: `DELETE /me` (borra el registro y los consentimientos) + C-05 para backups y logs |
| 11 | Restringir el uso de sus datos (máximo 2 datos) | ☐ | C-06: `POST /me/restricciones`, que acepta hasta 2 campos (p. ej. correo y apellidos) excluidos de marketing y analítica; se respeta en todas las consultas |
| **Seguridad de datos y protección** | | | |
| 13 | Cifrado en la BD | ☐ | C-02: AES-GCM sobre correo y teléfono; llave fuera del repo y del host de la BD |
| 14 | Contraseñas con hashing seguro | N/A hoy | No hay contraseñas. Si se agregan login o admin: Argon2id o bcrypt, nunca en texto plano |
| 15 | 2FA para cuentas administrativas | ☐ | C-01: el rol `admin` requiere TOTP para `GET /registros` |
| 16 | Firewall / protección contra intrusos | ☐ | C-08: solo se exponen los puertos 443 y 80→443; rate limiting en `/registro` |
| **Transparencia y políticas de privacidad** | | | |
| 18 | Apartado accesible en el front con la política | ☐ | C-04: enlace "Política de privacidad v1.0" en el formulario y en el pie |
| 19 | Política clara y fácil de entender | ☐ | C-04: aviso por capas (capa 1 de 2–3 líneas + política completa), que cubre el art. 18 |
| 20 | Informar cambios en la política | ☐ | C-04: `version_politica` en el consentimiento; si sube la versión con una finalidad nueva, se vuelve a pedir el consentimiento y se avisa por correo |
| **Integración de privacidad en el diseño** | | | |
| 22 | Privacidad desde el diseño inicial de la BD y el front | ✓ (parcial) | Esta DPIA se hizo antes del primer dato real. Ya aplicado: consultas parametrizadas y `.gitignore` |
| 23 | Considerar la privacidad en todas las decisiones de diseño | ☐ | La DPIA es un documento vivo: se repite al cambiar datos, finalidad o tecnología |
| 24 | Revisiones periódicas | ☐ | Revisión de la DPIA cada semestre o ante cada cambio + revisión cruzada (Paso 3) |
| 25 | Eliminar datos antiguos o innecesarios | ☐ | C-05: tarea semanal que borra 12 meses de inactividad y bajas > 30 días; logs a 90 días |
| **Extras** | | | |
| 27 | Descarga de todos los datos en formato legible | ☐ | C-06: `GET /me/export` (JSON, portabilidad) |
| 28 | Protocolo ante brechas | ☐ | C-09: procedimiento escrito, responsable designado y notificación a la ANPD en 48 h |
| 29 | Formación continua del equipo | ☐ | Medida administrativa: capacitación OWASP y Ley 29733 al ingresar y una vez al año |
