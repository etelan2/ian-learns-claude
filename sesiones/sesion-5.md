# Sesión 5 — Hacer que la cosa hable con el mundo

**Duración**: 90 minutos
**Entregable**: tu proyecto consume o sirve datos reales (API, archivo, BD)
**Meta-aprendizaje**: software vive en sistemas, no en archivos sueltos.

---

## Antes de empezar

- [ ] Tu proyecto tiene 1-2 features funcionando local
- [ ] Has resuelto al menos 3 bugs documentados

---

## Hoy tu proyecto cruza una frontera

Hasta hoy, tu proyecto vive en tu Mac. Hoy va a:
- Pedirle datos a otro sistema (API), O
- Guardar datos persistentes (BD, archivo), O
- Recibir datos de un usuario externo

Eso lo convierte en **software real**, no en script de tarea.

---

## Parte 1 (20 min) — Decidir qué "conexión" hacer

Pídele a Claude:

```
Mi proyecto hoy hace [X]. Para que sea más real, quiero conectarlo con algo del mundo exterior.

Tengo 3 opciones:
1. Consumir una API pública (ej: clima, frases, imágenes, lo que sea)
2. Guardar datos en un archivo local o base de datos
3. Recibir input del usuario via web/terminal

Para MI proyecto específico, ¿cuál tiene más sentido y por qué? Dame 3 opciones específicas y vota por una.
```

Lee su recomendación. Decide.

---

## Parte 2 (15 min) — Aprender el concepto

Si elegiste **API**:
```
Explícame qué es una API. ¿Cómo funciona el flujo cliente-servidor? Dame una analogía simple. Después muéstrame ejemplo de código simple en Python que llame a una API.
```

Si elegiste **BD**:
```
Explícame qué es una base de datos. Para mi proyecto, ¿qué tipo es mejor (SQLite, archivo JSON, otro)? Dame una analogía simple.
```

Si elegiste **input usuario**:
```
Explícame cómo recibir input de un usuario. ¿CLI, web form, ambos? Para mi proyecto, ¿cuál tiene sentido?
```

---

## Parte 3 (40 min) — Implementar

Construye la conexión. Mismas reglas de antes:
- Una pregunta a la vez a Claude
- Lee cada línea de código que él te dé
- Si no entiendes algo, pregúntale ANTES de copiar
- Cuando algo no funcione, pega el error textual

**Tip importante**: las API y BD requieren manejar **secretos** (API keys, contraseñas). NUNCA pongas estos en tu código directo. Pídele a Claude:

```
¿Cómo manejo correctamente las credenciales (API keys, passwords) en mi proyecto? Quiero hacerlo bien desde el principio.
```

Va a enseñarte sobre `.env` files y `.gitignore`. **Esa lección vale oro.**

---

## Parte 4 (10 min) — Verificar end-to-end

Una vez que funcione:

1. Borra los datos de prueba
2. Corre el flujo completo de cero
3. ¿Funciona?
4. ¿Hay algún caso edge que no manejaste? (datos vacíos, sin internet, formato raro)

Pídele a Claude:

```
Mi conexión funciona en el caso feliz. ¿Qué casos edge debería probar? Hazme una lista de 5 y los probamos juntos.
```

---

## Parte 5 (5 min) — Bitácora

`bitacora/sesion-5.md`:

1. Qué aprendí hoy
2. Qué me costó
3. Qué quiero hacer la próxima
4. **Conexión nueva**: ¿qué hace ahora mi proyecto que antes no podía?

Commit + push.

---

## Meta-lección

> Software que no habla con nada es script. Software que habla con sistemas externos es producto.

Lo que aprendiste hoy se llama **integración**. Es lo que separa a alguien que "sabe Python" de alguien que "construye productos".

Tu próximo proyecto va a tener integraciones desde el día 1. Es el patrón normal de 2026.

— Federico + Claude
