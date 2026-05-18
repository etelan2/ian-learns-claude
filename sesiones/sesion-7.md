# Sesión 7 — Enseñarle a Claude tu contexto

**Duración**: 90 minutos
**Entregable**: tu propio `CLAUDE.md` para tu proyecto
**Meta-aprendizaje**: AI sin contexto = AI tonto. La habilidad real es dar contexto.

---

## Antes de empezar

- [ ] Tu proyecto deployed con URL pública (sesión 6)
- [ ] Al menos 1 feedback recibido

---

## El secreto que pocos saben

La diferencia entre alguien que **usa** Claude y alguien que **trabaja** con Claude es **el contexto**.

Si abres una conversación con Claude vacía, te ayuda como cualquier persona random. Si abres una conversación con Claude que ya conoce:
- Quién eres
- Qué estás construyendo
- Tus preferencias técnicas
- Tu estilo de comunicación
- Las decisiones que ya tomaste

...te ayuda 10x mejor. Es como tener un colega que ya conoce tu proyecto vs un consultor externo que llega cada vez.

Hoy aprendes a darle ese contexto.

---

## Parte 1 (20 min) — Qué es CLAUDE.md

Pídele a Claude:

```
Explícame qué es un archivo CLAUDE.md. ¿Para qué sirve? ¿Cómo lo lee Claude Code? ¿Qué información típica va ahí? Muéstrame ejemplos cortos.
```

Lee con calma.

**Concepto clave**: cuando hay un `CLAUDE.md` en una carpeta, Claude Code lo lee automáticamente al iniciar. Es contexto persistente. No tienes que repetir cosas cada vez.

---

## Parte 2 (40 min) — Escribir tu CLAUDE.md

Vas a crear `CLAUDE.md` en la raíz de tu proyecto. Debe contener (mínimo):

### 1. Quién eres
```markdown
# CLAUDE.md — [Nombre de mi proyecto]

Soy Ian, 16 años, aprendiendo a programar.
Este proyecto es [descripción 1 línea].
```

### 2. Qué hace el proyecto
```markdown
## Qué hace
- [feature 1]
- [feature 2]
- [feature 3]
```

### 3. Stack técnico
```markdown
## Stack
- Lenguaje: [Python / Node / etc.]
- Framework: [si aplica]
- BD: [si aplica]
- Deploy: [Vercel / Render / etc.]
```

### 4. Tus preferencias
```markdown
## Cuando me ayudes
- Habla en español, de tú
- Explica las cosas como si tuviera 16 años (porque los tengo)
- NO me des código que no haya pedido
- Si me equivoco, dime POR QUÉ, no solo me corrijas
- Una pregunta a la vez
```

### 5. Decisiones ya tomadas
```markdown
## Decisiones que ya están tomadas
- Estamos usando [X] porque [razón]
- NO vamos a usar [Y] aunque parezca buena idea
- El scope mínimo es [Z]
```

### 6. Lo que NO sé todavía
```markdown
## Cosas que aún estoy aprendiendo
- [tema 1]
- [tema 2]
```

Escríbelo con tus palabras. Pídele a Claude que lo revise:

```
Aquí está mi CLAUDE.md. ¿Está claro? ¿Falta algo importante? ¿Hay algo redundante o que sobra?
```

Itera 2-3 veces hasta que esté limpio.

---

## Parte 3 (15 min) — Probar el efecto

Cierra Claude Code. Vuélvelo a abrir desde la raíz de tu proyecto. Empieza una conversación nueva:

```
Hola. ¿Sabes en qué estamos trabajando?
```

Claude debería responder con contexto real de tu proyecto, sin que tú se lo hayas dicho en esta conversación. **Ese momento es mágico.**

Pídele una mejora a tu proyecto. Compara la calidad de su respuesta vs sesiones anteriores. Ahora él sabe quién eres, qué estás construyendo, y cómo te gusta trabajar.

---

## Parte 4 (10 min) — Skills (avanzado, opcional)

Si te queda tiempo:

```
Claude Code tiene un concepto llamado "Skills". Explícame qué son. ¿Tiene sentido que yo cree uno para mi proyecto? ¿Cuál?
```

Si encaja, crea uno. Si no, déjalo para más adelante.

---

## Parte 5 (5 min) — Bitácora

`bitacora/sesion-7.md`:

1. Qué aprendí hoy
2. Qué me costó
3. **Antes de CLAUDE.md, mis conversaciones con Claude eran**: _______
4. **Después de CLAUDE.md, son**: _______
5. Qué quiero hacer la próxima

Commit + push.

---

## Meta-lección

> La habilidad más valuable de programar con AI en 2026 no es escribir prompts. Es construir contexto persistente que la AI pueda leer.

Lo que hiciste hoy se llama **context engineering**. Es lo nuevo. Hace 6 meses ni existía como término. En 2 años va a ser job description común.

Tú ya lo practicas. A los 16. Eso es valioso.

— Federico + Claude
