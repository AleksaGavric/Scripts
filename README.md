# Programming Experiments

A collection of small Python exercises and an unfinished Rust version-control experiment. This repository is learning history; the individual scripts are independent rather than a single application.

| File | Purpose / requirements |
| --- | --- |
| `fibonacci.py` | Iterator and floating-point closed-form comparison; large indices exceed the formula's numerical precision |
| `armstrong_number.py` | Three-digit Armstrong-number search |
| `letter_evolution.py` | Random character matching with retained correct positions |
| `website_alarm.py` | Local HH:MM alarm that opens a browser tab |
| `hilbert_curve.py`, `koch_fractal.py` | Recursive turtle graphics; desktop/Tk required |
| `random_turtle.py` | Turtle animation with rapid background changes; inspect before running |
| `gitclone.rs` | Incomplete revision/tracking-list sketch; no Cargo manifest is included |

## Run

For the Python examples, use Python 3 and run one script from this directory:

```sh
python3 fibonacci.py
python3 armstrong_number.py
python3 -m unittest discover -s tests
```

Most Python scripts use only the standard library. Turtle examples require a graphical display and a Python installation with Tk support. The Koch example uses a large recursion workload; reduce its parameters for exploration. The alarm remains a local process and does not schedule an operating-system notification.

`gitclone.rs` is a source sketch using `chrono` and `sha2`; it is not a Git replacement or a runnable Cargo project. Its placeholder filesystem paths require adaptation.
