# Sesión 1 — Hola Claude

**Duración**: 90 minutos
**Entregable**: Claude Code instalado en tu Mac + primer "hola mundo" + cuenta de Claude funcionando
**Meta-aprendizaje**: La AI no es un buscador. Es un colega que habla contigo.

---

## Antes de empezar

Asegúrate de tener:
- [ ] Tu Mac contigo, prendida, con WiFi funcionando
- [ ] Tu correo personal a la mano (vas a crear cuentas)
- [ ] Una hora y media libre sin interrupciones

---

## Parte 1 (15 min) — Crear tu cuenta de Claude

1. Abre Safari o Chrome
2. Ve a **claude.ai**
3. Haz clic en "Sign up"
4. Usa tu correo personal
5. Crea tu password (algo seguro que recuerdes — apúntalo en un papel físico, NO en una nota de la compu)
6. Confirma tu correo

**Federico te va a dar la cuenta upgrade a Pro ($20 USD/mes) — eso te desbloquea Claude Code.**

---

## Parte 2 (20 min) — Instalar Claude Code en tu Mac

Vas a abrir la **Terminal** (la app que parece pantalla negra con texto). Para abrirla:

1. Pulsa `Cmd + Space`
2. Escribe "Terminal"
3. Enter

Verás algo así:
```
ian@MacBook ~ %
```

Ese símbolo `%` significa "la computadora te está esperando, escribe algo".

### Instalar Claude Code

Copia y pega ESTA línea (tal cual, sin cambiar nada):

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Pulsa Enter. Va a tardar 1-2 minutos.

### Hacer login

Cuando termine de instalar, escribe:

```bash
claude
```

Te va a pedir login. Sigue las instrucciones que aparezcan en pantalla — te va a abrir el navegador, conectas tu cuenta de claude.ai, y listo.

### Verifica que funcionó

Escribe:

```bash
claude --version
```

Si te sale un número de versión (algo como `2.x.x`), funcionó. **Si te sale error, pídele ayuda a Claude.**

---

## Parte 3 (10 min) — Tu primera conversación con Claude

Estando en la Terminal, escribe:

```bash
claude
```

Vas a entrar a una conversación con Claude. Escribe esto exactamente:

```
Hola Claude, soy Ian. Tengo 16 años y estoy aprendiendo a programar contigo. Soy ex-alumno de Federico Peña en la escuela Algorítmica. ¿Me explicas brevemente qué es lo que vas a poder hacer conmigo durante este curso?
```

Lee lo que te conteste. **NO escribas la siguiente cosa hasta que termines de leer.**

Cuando hayas leído, escríbele:

```
¿Cuál es la diferencia entre tú y Google? Cuando le pregunto a Google algo, me da páginas. Cuando te pregunto a ti, me das ¿qué exactamente?
```

Lee lo que te conteste. **El meta-aprendizaje aquí**: estás aprendiendo a hablarle a una AI en lenguaje natural. No es un buscador. Es un colega.

---

## Parte 4 (30 min) — Tu primer "Hola Mundo"

Vamos a hacer que tu computadora diga "Hola, mundo" pero a tu manera.

Pídele a Claude:

```
Quiero que mi Mac me diga "Hola, mundo" pero en español, con mi nombre, y de una forma divertida. Soy Ian. No me des el código todavía — primero pregúntame qué tipo de "divertida" quiero.
```

Claude te va a preguntar qué te late. Tú decide:
- ¿Texto colorido?
- ¿Que parezca una conversación?
- ¿Que tenga emojis?
- ¿Otra cosa que se te ocurra?

Cuando le respondas, Claude te va a hacer el código. **Léelo línea por línea con él**. Si no entiendes algo, pregúntale:

```
Espérate, ¿qué hace esta línea? Explícamela como si tuviera 12 años.
```

Cuando entiendas, guárdalo en un archivo. Pídele:

```
Ayúdame a guardar esto en un archivo llamado hola.py. ¿Cómo lo hago paso a paso?
```

Ejecuta el programa. Pídele:

```
¿Cómo lo ejecuto desde Terminal?
```

**Cuando funcione**: tómate una foto del resultado en pantalla. Mándasela a Federico. Es un momento histórico — es tu primer programa real.

---

## Parte 5 (10 min) — Bitácora

Abre tu editor (te explico cuál en la próxima sesión — por ahora puedes usar la app **Notas** de tu Mac).

Crea una nota con el título "Sesión 1 — Hola Claude" y escribe (mínimo) tres frases:

1. **Qué aprendí hoy**:
2. **Qué me costó**:
3. **Qué quiero hacer la próxima**:

Mándale screenshot a Federico de tu bitácora. Eso es tu cierre de sesión.

---

## Si te atoraste

- **Si el comando no funciona**: pregúntale a Claude directamente. Copia y pega el error que te salió.
- **Si Claude te dice algo que no entiendes**: contéstale "explícamelo más simple".
- **Si te frustras**: cierra la laptop 5 minutos. Vuelve. La frustración es normal.
- **Si nada funciona después de 15 min**: escríbele a Federico. No te quedes media hora trabado.

---

## Meta-lección de esta sesión

La AI **no sabe lo que tú quieres** hasta que se lo dices. La habilidad más importante que vas a aprender en este curso es:

> **Saber explicarle a una AI qué quieres construir, paso a paso, en tus propias palabras.**

Eso no se aprende en una sesión. Se aprende en 8. Pero ya empezaste.

Bienvenido al curso, Ian. Bienvenido al 2026.

— Federico + Claude
