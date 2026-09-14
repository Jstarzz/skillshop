# Recording contract

Capture **semantics before coordinates**. A useful recording should survive harmless layout changes.

When available, retain: route/URL, viewport or device, accessibility role/name, stable test id, semantic action, relevant network method/path/status/timing, console exceptions, screenshots/evidence references, and business assertions.

## Redaction
Never persist raw passwords, session cookies, `Authorization` headers, private API keys, full payment-card data, or secrets from local storage. Replace them with symbolic values such as `${SESSION}` or `${CARD_TEST_TOKEN}`.

## Dynamic values
Mark generated IDs, CSRF values, timestamps, order/payment references, and other values that must be extracted and reused. The journey compiler must parameterize these instead of hard-coding one recording.

## Recording modes
- **Human recording:** capture what a tester actually does, then annotate intent.
- **Agent recording:** the agent records its own exploration while preserving the same semantic schema.
- **Manual authoring:** create a semantic journey directly when no browser recorder is available.
