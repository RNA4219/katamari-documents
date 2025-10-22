
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
|  src/app.py (thin wiring)                    |
|  - apply_settings()                          |
|  - on_message(): prethought->persona->trim->chain->provider
+---------+-------------------------+----------+
          |                         |
          v                         v
  +-------+------+           +------+---------+
  | src/core_ext/* |         | src/providers/* |
  | persona      |           | openai, gemini|
  | trimmer      |           +----------------+
  | prethought   |
  | multistep    |
  | logging      |
  | retention (M1 計画中) |
  | evolve (M2)  |
  +--------------+
```
