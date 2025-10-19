
# Architecture (ASCII)
```
+-------------------+        +-------------------+
|  Chainlit UI      |        |  Chat Settings    |
| - Chat/Steps/SSE  |<-----> | - model/chain     |
+---------+---------+        | - trim/persona    |
          |                  +---------+---------+
          | SSE/JSON                           |
          v                                    v
+---------+------------------------------------+
|  app.py (thin wiring)                        |
|  - apply_settings()                          |
|  - on_message(): prethought->persona->trim->chain->provider
+---------+-------------------------+----------+
          |                         |
          v                         v
  +-------+------+           +------+---------+
  | core_ext/*   |           | providers/*   |
  | persona      |           | openai, gemini|
  | trimmer      |           +----------------+
  | prethought   |
  | multistep    |
  | evolve (M2)  |
  +--------------+
```
