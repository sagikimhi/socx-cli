# socx

Aggregate public SoCX APIs to provide a concise import surface.

Modules:

- **`cli`** – Expose primary CLI entry points and shared helpers.
- **`cli_cfg`** – Configuration and theme defaults for the SoCX CLI.
- **`config`** – Aggregate configuration utilities and metadata for SoCX.
- **`console`** – Preconfigured Rich console used throughout SoCX.
- **`io`** – Expose logging, console, and decorator utilities for I/O facilities.
- **`log`** – Logging helpers that standardise Rich-powered output across SoCX.
- **`patterns`** – Expose reusable design-pattern utilities leveraged throughout SoCX.
- **`regression`** – Expose regression primitives for use throughout SoCX.

Classes:

- **`BottomUpTraversal`** – Post-order traversal that visits descendants before parents.
- **`ByLevelTraversal`** – Breadth-first traversal that visits nodes one level at a time.
- **`CompileConverter`** – Compile python source files referenced in configuration values.
- **`Converter`** – Base protocol for Dynaconf converters used by SoCX.
- **`Formatter`** – Base callable used to format configuration objects for display.
- **`ImportConverter`** – Import modules referenced in configuration entries.
- **`Level`** – Log level enumeration mirroring the standard library constants.
- **`Node`** – Protocol for nodes that accept visitors.
- **`PathConverter`** – Resolve string inputs into concrete filesystem paths.
- **`PtrMixin`** – Pointer mixin class.
- **`Regression`** – Manage and execute a collection of tests with concurrency control.
- **`Singleton`** – Mixin class for creating singleton classes.
- **`Structure`** – Protocol for structures exposing child relationships.
- **`SymbolConverter`** – Resolve dotted path:attribute references or file symbols.
- **`Test`** – Holds information about a test.
- **`TestBase`** – Provide common process-management behaviour for regression tests.
- **`TestCommand`** – Represent a test invocation parsed from a command-line string.
- **`TestResult`** – Represents the result of a test that had finished and exited normally.
- **`TestStatus`** – TestStatus representation of a test process as an IntEnum.
- **`TopDownTraversal`** – Pre-order traversal that visits parents before descendants.
- **`Traversal`** – Adapter interface that controls how nodes accept visitors.
- **`TreeFormatter`** – Format Dynaconf settings into an inspectable tree view.
- **`UIDMixin`** – Unique instance ID mixin class.
- **`Visitor`** – Protocol describing objects that can visit nodes.

Functions:

- **`add_converters`** – Register converters with Dynaconf using their inferred names.
- **`add_filter`** – Attach a filter to the module-level logger.
- **`add_handler`** – Attach handler to the module-level logger.
- **`add_options`** – Compose multiple option decorators into a single decorator.
- **`get_converters`** – Yield converter registrations, wrapping raw callables as needed.
- **`get_handler`** – Return a handler registered under name if one exists.
- **`get_handler_names`** – Return the names of all registered logging handlers.
- **`get_level`** – Return the effective log level for logger\_ as a Level enum.
- **`get_logger`** – Return a child logger configured with optional file output.
- **`global_options`** – Apply the standard set of global SoCX CLI options.
- **`has_handlers`** – Return True if the module-level logger has active handlers.
- **`is_enabled_for`** – Return True if the module-level logger handles level.
- **`log_it`** – Add automatic entered/returned logging to decorated callables.
- **`remove_filter`** – Detach a filter from the module-level logger.
- **`remove_handler`** – Remove handler from the module-level logger.
- **`set_level`** – Set the log level on the provided logger (defaults to module logger).
- **`validate_all`** – Run validation against all registered validators.

Attributes:

- **`APP_CONFIG_DIR`** (`Path`) – Path to application's settings files directory.
- **`APP_CONFIG_FILE`** (`Path`) – File path to application's main settings file.
- **`APP_STATIC_DIR`** (`Path`) – Path to application's static files directory.
- **`APP_TEMPLATES_DIR`** (`Path`) – Path to application's template files directory.
- **`AnyCallable`** –
- **`DEFAULT_FORMAT`** (`Final[str]`) – Default log message format used by the root handler.
- **`DEFAULT_HANDLERS`** (`Final[list[Handler]]`) – Handlers attached to the module-level logger by default.
- **`DEFAULT_LEVEL`** (`Final[Level]`) – Default logger level, a.k.a verbosity.
- **`DEFAULT_TIME_FORMAT`** (`Final[str]`) – Default timestamp format injected into log records.
- **`Decorator`** –
- **`USER_CACHE_DIR`** (`Path`) – Absolute path to platform's native application cache directory.
- **`USER_CONFIG_DIR`** (`Path`) – Absolute path to platform's native application config directory.
- **`USER_CONFIG_FILE`** (`Path`) – Absolute path to application's user config file.
- **`USER_DATA_DIR`** (`Path`) – Absolute path to platform's native application data directory.
- **`USER_LOG_DIR`** (`Path`) – Absolute path to platform's native application logs directory.
- **`USER_LOG_FILE`** (`Path`) – Absolute path to application's main log for the current local user.
- **`USER_RUNTIME_DIR`** (`Path`) – Absolute path to platform's native application runtime directory.
- **`USER_STATE_DIR`** (`Path`) – Absolute path to platform's native application state directory.
- **`logger`** – Default logging handler.
- **`settings`** (`Settings`) –

## APP_CONFIG_DIR

```
APP_CONFIG_DIR: Path = APP_STATIC_DIR / 'settings'
```

Path to application's settings files directory.

## APP_CONFIG_FILE

```
APP_CONFIG_FILE: Path = APP_CONFIG_DIR / 'settings.yaml'
```

File path to application's main settings file.

## APP_STATIC_DIR

```
APP_STATIC_DIR: Path = __directory__ / 'static'
```

Path to application's static files directory.

## APP_TEMPLATES_DIR

```
APP_TEMPLATES_DIR: Path = __directory__ / 'templates'
```

Path to application's template files directory.

## AnyCallable

```
AnyCallable = Callable[..., Any]
```

## DEFAULT_FORMAT

```
DEFAULT_FORMAT: Final[str] = get(
    "SOCX_LOG_FORMAT", "%(message)s"
)
```

Default log message format used by the root handler.

## DEFAULT_HANDLERS

```
DEFAULT_HANDLERS: Final[list[Handler]] = [
    _get_console_handler(DEFAULT_LEVEL),
    _get_file_handler(
        DEFAULT_LOG_DIRECTORY / DEFAULT_LOG_FILE
    ),
]
```

Handlers attached to the module-level logger by default.

## DEFAULT_LEVEL

```
DEFAULT_LEVEL: Final[Level] = Level[
    get("SOCX_VERBOSITY", "INFO")
]
```

Default logger level, a.k.a verbosity.

## DEFAULT_TIME_FORMAT

```
DEFAULT_TIME_FORMAT: Final[str] = get(
    "SOCX_TIME_FORMAT", "[%x %X]"
)
```

Default timestamp format injected into log records.

## Decorator

```
Decorator = Callable[[FuncType], FuncType]
```

## USER_CACHE_DIR

```
USER_CACHE_DIR: Path = resolve()
```

Absolute path to platform's native application cache directory.

## USER_CONFIG_DIR

```
USER_CONFIG_DIR: Path = resolve()
```

Absolute path to platform's native application config directory.

## USER_CONFIG_FILE

```
USER_CONFIG_FILE: Path = (
    USER_CONFIG_DIR / USER_CONFIG_FILENAME
)
```

Absolute path to application's user config file.

## USER_DATA_DIR

```
USER_DATA_DIR: Path = resolve()
```

Absolute path to platform's native application data directory.

## USER_LOG_DIR

```
USER_LOG_DIR: Path = resolve()
```

Absolute path to platform's native application logs directory.

## USER_LOG_FILE

```
USER_LOG_FILE: Path = USER_LOG_DIR / USER_LOG_FILENAME
```

Absolute path to application's main log for the current local user.

## USER_RUNTIME_DIR

```
USER_RUNTIME_DIR: Path = resolve()
```

Absolute path to platform's native application runtime directory.

## USER_STATE_DIR

```
USER_STATE_DIR: Path = resolve()
```

Absolute path to platform's native application state directory.

## logger

```
logger = _get_logger()
```

Default logging handler.

Can be used for default logging when no custom behavior is required.

Generally, it is recommended to use the `get_logger` method instead of the default logger whenever your application requires something a bit more complex or extensive than a basic write to console functionality.

## settings

```
settings: Settings = get_settings()
```

## BottomUpTraversal

Post-order traversal that visits descendants before parents.

Methods:

- **`accept`** – Traverse child subtrees prior to visiting n.

### accept

```
accept(
    n: NODE, v: Visitor[NODE], p: Structure[NODE]
) -> None
```

Traverse child subtrees prior to visiting `n`.

Source code in `src/socx/patterns/visitor/traversal.py`

```
@classmethod
def accept(cls, n: NODE, v: Visitor[NODE], p: Structure[NODE]) -> None:
    """Traverse child subtrees prior to visiting ``n``."""
    for c in p.children(n):
        cls.accept(c, v, p)

    v.visit(n)
```

## ByLevelTraversal

Breadth-first traversal that visits nodes one level at a time.

Methods:

- **`accept`** – Walk the structure level-by-level starting from n.

### accept

```
accept(
    n: NODE, v: Visitor[NODE], p: Structure[NODE]
) -> None
```

Walk the structure level-by-level starting from `n`.

Source code in `src/socx/patterns/visitor/traversal.py`

```
@classmethod
def accept(cls, n: NODE, v: Visitor[NODE], p: Structure[NODE]) -> None:
    """Walk the structure level-by-level starting from ``n``."""
    q: list[NODE] = [n]

    while q:
        t: list[NODE] = []

        for n_ in q:
            v.visit(n_)
            t.extend(p.children(n_))

        q = t
```

## CompileConverter

Compile python source files referenced in configuration values.

Methods:

- **`error`** – Log a recoverable converter error message.
- **`exception`** – Log a conversion failure with context for debugging.

Attributes:

- **`name`** (`str`) – Return the registered converter name inferred from the class.

### name

```
name: str
```

Return the registered converter name inferred from the class.

### error

```
error(error: str) -> None
```

Log a recoverable converter error message.

Source code in `src/socx/config/converters.py`

```
def error(self, error: str) -> None:
    """Log a recoverable converter error message."""
    logger.error(f"Converter({self.name}): {error}")
```

### exception

```
exception(value: str) -> None
```

Log a conversion failure with context for debugging.

Source code in `src/socx/config/converters.py`

```
def exception(self, value: str) -> None:
    """Log a conversion failure with context for debugging."""
    logger.exception(
        f"Converter({self.name}): failed to convert value '{value}'"
    )
```

## Converter

Base protocol for Dynaconf converters used by SoCX.

Methods:

- **`error`** – Log a recoverable converter error message.
- **`exception`** – Log a conversion failure with context for debugging.

Attributes:

- **`name`** (`str`) – Return the registered converter name inferred from the class.

### name

```
name: str
```

Return the registered converter name inferred from the class.

### error

```
error(error: str) -> None
```

Log a recoverable converter error message.

Source code in `src/socx/config/converters.py`

```
def error(self, error: str) -> None:
    """Log a recoverable converter error message."""
    logger.error(f"Converter({self.name}): {error}")
```

### exception

```
exception(value: str) -> None
```

Log a conversion failure with context for debugging.

Source code in `src/socx/config/converters.py`

```
def exception(self, value: str) -> None:
    """Log a conversion failure with context for debugging."""
    logger.exception(
        f"Converter({self.name}): failed to convert value '{value}'"
    )
```

## Formatter

Base callable used to format configuration objects for display.

## ImportConverter

Import modules referenced in configuration entries.

Methods:

- **`error`** – Log a recoverable converter error message.
- **`exception`** – Log a conversion failure with context for debugging.

Attributes:

- **`name`** (`str`) – Return the registered converter name inferred from the class.

### name

```
name: str
```

Return the registered converter name inferred from the class.

### error

```
error(error: str) -> None
```

Log a recoverable converter error message.

Source code in `src/socx/config/converters.py`

```
def error(self, error: str) -> None:
    """Log a recoverable converter error message."""
    logger.error(f"Converter({self.name}): {error}")
```

### exception

```
exception(value: str) -> None
```

Log a conversion failure with context for debugging.

Source code in `src/socx/config/converters.py`

```
def exception(self, value: str) -> None:
    """Log a conversion failure with context for debugging."""
    logger.exception(
        f"Converter({self.name}): failed to convert value '{value}'"
    )
```

## Level

Log level enumeration mirroring the standard library constants.

Attributes:

- **`CRITICAL`** –
- **`DEBUG`** –
- **`ERROR`** –
- **`FATAL`** –
- **`INFO`** –
- **`NOTSET`** –
- **`WARN`** –
- **`WARNING`** –

### CRITICAL

```
CRITICAL = 50
```

### DEBUG

```
DEBUG = 10
```

### ERROR

```
ERROR = 40
```

### FATAL

```
FATAL = 50
```

### INFO

```
INFO = 20
```

### NOTSET

```
NOTSET = 0
```

### WARN

```
WARN = 30
```

### WARNING

```
WARNING = 30
```

## Node

Protocol for nodes that accept visitors.

Methods:

- **`accept`** – Accept a visit from a Visitor.

### accept

```
accept(v: Visitor[NODE]) -> None
```

Accept a visit from a `Visitor`.

Source code in `src/socx/patterns/visitor/protocol.py`

```
def accept(self, v: Visitor[NODE]) -> None:
    """Accept a visit from a `Visitor`."""
    ...
```

## PathConverter

Resolve string inputs into concrete filesystem paths.

Methods:

- **`error`** – Log a recoverable converter error message.
- **`exception`** – Log a conversion failure with context for debugging.

Attributes:

- **`name`** (`str`) – Return the registered converter name inferred from the class.

### name

```
name: str
```

Return the registered converter name inferred from the class.

### error

```
error(error: str) -> None
```

Log a recoverable converter error message.

Source code in `src/socx/config/converters.py`

```
def error(self, error: str) -> None:
    """Log a recoverable converter error message."""
    logger.error(f"Converter({self.name}): {error}")
```

### exception

```
exception(value: str) -> None
```

Log a conversion failure with context for debugging.

Source code in `src/socx/config/converters.py`

```
def exception(self, value: str) -> None:
    """Log a conversion failure with context for debugging."""
    logger.exception(
        f"Converter({self.name}): failed to convert value '{value}'"
    )
```

## PtrMixin

Pointer mixin class.

Extending this class adds the `ref` property to subclass instances and the `dref` class method to the subclass.

Methods:

- **`dref`** – Dereference a stored UID and return the tracked instance.

Attributes:

- **`ref`** (`int`) – Return the object's assigned unique identifier.

### ref

```
ref: int
```

Return the object's assigned unique identifier.

### dref

```
dref(ref: int) -> UIDBase | None
```

Dereference a stored UID and return the tracked instance.

Source code in `src/socx/patterns/mixins/uid.py`

```
@classmethod
def dref(cls, ref: int) -> UIDBase | None:
    """Dereference a stored UID and return the tracked instance."""
    return UIDBase._get_inst(ref)
```

## Regression

```
Regression(
    name: str,
    tests: Iterable[TestType],
    *args: Any,
    **kwargs: Any,
)
```

Manage and execute a collection of tests with concurrency control.

Methods:

- **`accept`** – Accept a visit from a Visitor.
- **`from_lines`** – Construct a regression from serialized command lines.
- **`interrupt`** – Interrupt the execution of a running test with a SIGINT signal.
- **`kill`** – Interrupt the execution of a running test with a SIGKILL signal.
- **`resume`** – Resume the execution of a paused test.
- **`start`** – Start the regression.
- **`suspend`** – Suspend the execution of a running test.
- **`terminate`** – Interrupt the execution of a running test with a SIGTERM signal.
- **`wait`** – Wait for a test to terminate if it is running.

Attributes:

- **`cfg`** (`DynaBox`) – Return the regression configuration namespace.
- **`command`** (`TestCommand`) – Test execution command representation as an object.
- **`finished_time`** (`str`) – Return the formatted timestamp captured when the test finished.
- **`messages`** (`Queue`) –
- **`name`** (`str`) – Return the test's human readable name.
- **`options`** (`DynaBox`) – Return the nested options block under the regression settings.
- **`pending`** (`Queue`) –
- **`pid`** (`int`) – Return the process identifier for the test's subprocess.
- **`progress`** – Expose the Progress instance tracking regression status.
- **`result`** – Return the result enum once a test has completed.
- **`run_limit`** (`int`) – Return the maximum number of tests that may run concurrently.
- **`started_time`** (`str`) – Return the formatted timestamp captured when the test started.
- **`status`** (`TestStatus`) – Return the current lifecycle status of the test.
- **`tests`** (`deque[Test]`) – An iterable of all tests defined in the regression.

Source code in `src/socx/regression/regression.py`

```
def __init__(
    self, name: str, tests: Iterable[TestType], *args: Any, **kwargs: Any
) -> None:
    TestBase.__init__(self, name, *args, **kwargs)
    tests = set(tests)
    self._lock = RLock()
    self._tests = deque(set(tests))
    self._runner_tid = None
    self._scheduler_tid = None
    self._regression_tid = None
    self._num_tests = len(self._tests)
    self._progress: Progress = Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        TaskProgressColumn(),
        BarColumn(),
        "[green]Completed:",
        MofNCompleteColumn(),
        "[yellow]Elapsed:",
        TimeElapsedColumn(),
        "[cyan]Remaining:",
        TimeRemainingColumn(),
        transient=False,
        expand=False,
    )
    self.pending: aio.Queue = aio.Queue(self.run_limit)
    self.messages: aio.Queue = aio.Queue()
```

### cfg

```
cfg: DynaBox
```

Return the regression configuration namespace.

### command

```
command: TestCommand
```

Test execution command representation as an object.

### finished_time

```
finished_time: str
```

Return the formatted timestamp captured when the test finished.

### messages

```
messages: Queue = Queue()
```

### name

```
name: str
```

Return the test's human readable name.

### options

```
options: DynaBox
```

Return the nested options block under the regression settings.

### pending

```
pending: Queue = Queue(run_limit)
```

### pid

```
pid: int
```

Return the process identifier for the test's subprocess.

### progress

```
progress
```

Expose the `Progress` instance tracking regression status.

### result

```
result
```

Return the result enum once a test has completed.

### run_limit

```
run_limit: int
```

Return the maximum number of tests that may run concurrently.

### started_time

```
started_time: str
```

Return the formatted timestamp captured when the test started.

### status

```
status: TestStatus
```

Return the current lifecycle status of the test.

### tests

```
tests: deque[Test]
```

An iterable of all tests defined in the regression.

### accept

```
accept(v: Visitor[TestABC]) -> None
```

Accept a visit from a `Visitor`.

Source code in `src/socx/regression/test.py`

```
@override
def accept(self, v: Visitor[TestABC]) -> None:
    """Accept a visit from a `Visitor`."""
    v.visit(self)
```

### from_lines

```
from_lines(
    name: str, lines: Iterable[str], test_cls: type = Test
) -> Regression
```

Construct a regression from serialized command lines.

Source code in `src/socx/regression/regression.py`

```
@classmethod
def from_lines(
    cls, name: str, lines: Iterable[str], test_cls: type = Test
) -> Regression:
    """Construct a regression from serialized command lines."""
    tests = [test_cls(line) for line in lines]
    return Regression(name, tests)
```

### interrupt

```
interrupt() -> None
```

Interrupt the execution of a running test with a SIGINT signal.

Source code in `src/socx/regression/regression.py`

```
@override
def interrupt(self) -> None:
    """Interrupt the execution of a running test with a SIGINT signal."""
    for test in self.tests:
        test.interrupt()
```

### kill

```
kill() -> None
```

Interrupt the execution of a running test with a SIGKILL signal.

Source code in `src/socx/regression/regression.py`

```
@override
def kill(self) -> None:
    """Interrupt the execution of a running test with a SIGKILL signal."""
    for test in self.tests:
        test.kill()
```

### resume

```
resume() -> None
```

Resume the execution of a paused test.

Source code in `src/socx/regression/regression.py`

```
@override
def resume(self) -> None:
    """Resume the execution of a paused test."""
    for test in self.tests:
        test.resume()
```

### start

```
start() -> None
```

Start the regression.

Source code in `src/socx/regression/regression.py`

```
@override
async def start(self) -> None:
    """Start the regression."""
    self._status = TestStatus.Pending
    logger.info("regression starting.")
    logger.debug(f"{self=}")
    self._started_time = time.perf_counter()

    try:
        async with aio.TaskGroup() as tg:
            self._status = TestStatus.Running
            tg.create_task(self._animate_progress())
            tg.create_task(self._schedule_tests())
            tg.create_task(self._run_tests())
    except Exception:
        self._status = TestStatus.Terminated
        self._result = TestResult.Failed
        raise
    else:
        self._status = TestStatus.Finished
        self._result = (
            TestResult.Passed
            if all(test.passed for test in self)
            else TestResult.Failed
        )
    finally:
        self._finished_time = time.perf_counter()
        logger.info("regression ending.")
        logger.debug(f"{self=}")
```

### suspend

```
suspend() -> None
```

Suspend the execution of a running test.

Source code in `src/socx/regression/regression.py`

```
@override
def suspend(self) -> None:
    """Suspend the execution of a running test."""
    for test in self.tests:
        test.suspend()
```

### terminate

```
terminate() -> None
```

Interrupt the execution of a running test with a SIGTERM signal.

Source code in `src/socx/regression/regression.py`

```
@override
def terminate(self) -> None:
    """Interrupt the execution of a running test with a SIGTERM signal."""
    for test in self.tests:
        test.terminate()
```

### wait

```
wait(timeout: float | None = None) -> None
```

Wait for a test to terminate if it is running.

Source code in `src/socx/regression/test.py`

```
def wait(self, timeout: float | None = None) -> None:
    """Wait for a test to terminate if it is running."""
    ...
```

## Singleton

Mixin class for creating singleton classes.

Extending this class enforces the singleton pattern on the subclass.

## Structure

Protocol for structures exposing child relationships.

Methods:

- **`children`** – Return the immediate children of s.

### children

```
children(s: NODE) -> Iterable[NODE]
```

Return the immediate children of `s`.

Source code in `src/socx/patterns/visitor/protocol.py`

```
@classmethod
def children(cls, s: NODE) -> Iterable[NODE]:
    """Return the immediate children of ``s``."""
    ...
```

## SymbolConverter

```
SymbolConverter()
```

Resolve dotted `path:attribute` references or file symbols.

Methods:

- **`error`** – Log a recoverable converter error message.
- **`exception`** – Log a conversion failure with context for debugging.

Attributes:

- **`compiler`** –
- **`evaluator`** –
- **`importer`** –
- **`name`** (`str`) – Return the registered converter name inferred from the class.

Source code in `src/socx/config/converters.py`

```
def __init__(self) -> None:
    self.importer = ImportConverter()
    self.compiler = CompileConverter()
    self.evaluator = EvalConverter()
```

### compiler

```
compiler = CompileConverter()
```

### evaluator

```
evaluator = EvalConverter()
```

### importer

```
importer = ImportConverter()
```

### name

```
name: str
```

Return the registered converter name inferred from the class.

### error

```
error(error: str) -> None
```

Log a recoverable converter error message.

Source code in `src/socx/config/converters.py`

```
def error(self, error: str) -> None:
    """Log a recoverable converter error message."""
    logger.error(f"Converter({self.name}): {error}")
```

### exception

```
exception(value: str) -> None
```

Log a conversion failure with context for debugging.

Source code in `src/socx/config/converters.py`

```
def exception(self, value: str) -> None:
    """Log a conversion failure with context for debugging."""
    logger.exception(
        f"Converter({self.name}): failed to convert value '{value}'"
    )
```

## Test

```
Test(command: str | TestCommand, *args, **kwargs)
```

Holds information about a test.

Methods:

- **`accept`** – Accept a visit from a Visitor.
- **`dref`** – Dereference a stored UID and return the tracked instance.
- **`interrupt`** – Interrupt the execution of a running test with a SIGINT signal.
- **`kill`** – Kill the process with SIGKILL as a last resort.
- **`resume`** – Resume the process if it is paused (sends a SIGCONT signal).
- **`start`** – Start a test in a subprocess.
- **`suspend`** – Send a SIGSTOP signal to suspend the test's running process.
- **`terminate`** – Terminate the process with SIGTERM.
- **`wait`** – Wait for a test to terminate if it is running.

Attributes:

- **`build`** (`str`) – Return the randomisation build identifier, if provided.
- **`cfg`** (`DynaBox`) –
- **`command`** (`TestCommand`) – Test execution command representation as an object.
- **`dirname`** – Return the directory name derived from the test identifier.
- **`failed`** (`bool`) – Return True if the test finished with a failure result.
- **`finished`** (`bool`) – Return True if the test completed and recorded a result.
- **`finished_time`** (`str`) – Return the formatted timestamp captured when the test finished.
- **`flow`** (`str`) – Return the execution flow name extracted from the command.
- **`idle`** (`bool`) – True if test has no active process and has not yet started.
- **`name`** (`str`) – Return the test's human readable name.
- **`passed`** (`bool`) – Return True if the test finished successfully.
- **`pending`** – Return True if the test is queued but not yet running.
- **`pid`** (`int`) – Return the process identifier for the test's subprocess.
- **`process`** (`Process`) – Return a psutil.Process wrapper for the test's subprocess.
- **`ref`** (`int`) – Return the object's assigned unique identifier.
- **`result`** – Return the result enum once a test has completed.
- **`returncode`** (`int | None`) – The return code from the test process or None if running or idle.
- **`running`** (`bool`) – True if test is currently running in a dedicated process.
- **`runtime_cfg`** (`DynaBox`) – Return the runtime settings section for this test.
- **`runtime_logs`** – Return the path where the simulator writes log files.
- **`runtime_path`** (`Path`) – Return the resolved runtime directory for this test instance.
- **`seed`** (`int`) – Return the randomisation seed for the test.
- **`started`** (`bool`) – Return True once start has spawned the subprocess.
- **`started_time`** (`str`) – Return the formatted timestamp captured when the test started.
- **`status`** (`TestStatus`) – Return the current lifecycle status of the test.
- **`stderr`** (`str | None`) – Return captured standard error once the test has finished.
- **`stdin`** (`str | None`) – Return None; subclasses may override to expose stdin.
- **`stdout`** (`str | None`) – Return captured standard output once the test has finished.
- **`suspended`** (`bool`) – Return True if the subprocess is currently stopped.
- **`terminated`** (`bool`) – Return True if the test ended due to termination signals.
- **`uid`** (`property`) –

Source code in `src/socx/regression/test.py`

```
@override
def __init__(self, command: str | TestCommand, *args, **kwargs) -> None:
    TestBase.__init__(self, command, *args, **kwargs)
    UIDMixin.__init__(self)

    try:
        name = self.command.test
    except AttributeError:
        self._missing_test_name_err(command)
        raise

    if "/" in name:
        name = name.partition("/")[-1]

    self._name = name
    self._seed = 0
    self._flow = None
    self._build = None
```

### build

```
build: str
```

Return the randomisation build identifier, if provided.

### cfg

```
cfg: DynaBox
```

### command

```
command: TestCommand
```

Test execution command representation as an object.

### dirname

```
dirname
```

Return the directory name derived from the test identifier.

### failed

```
failed: bool
```

Return `True` if the test finished with a failure result.

### finished

```
finished: bool
```

Return `True` if the test completed and recorded a result.

### finished_time

```
finished_time: str
```

Return the formatted timestamp captured when the test finished.

### flow

```
flow: str
```

Return the execution flow name extracted from the command.

### idle

```
idle: bool
```

True if test has no active process and has not yet started.

### name

```
name: str
```

Return the test's human readable name.

### passed

```
passed: bool
```

Return `True` if the test finished successfully.

### pending

```
pending
```

Return `True` if the test is queued but not yet running.

### pid

```
pid: int
```

Return the process identifier for the test's subprocess.

### process

```
process: Process
```

Return a `psutil.Process` wrapper for the test's subprocess.

### ref

```
ref: int
```

Return the object's assigned unique identifier.

### result

```
result
```

Return the result enum once a test has completed.

### returncode

```
returncode: int | None
```

The return code from the test process or None if running or idle.

### running

```
running: bool
```

True if test is currently running in a dedicated process.

### runtime_cfg

```
runtime_cfg: DynaBox
```

Return the runtime settings section for this test.

### runtime_logs

```
runtime_logs
```

Return the path where the simulator writes log files.

### runtime_path

```
runtime_path: Path
```

Return the resolved runtime directory for this test instance.

### seed

```
seed: int
```

Return the randomisation seed for the test.

### started

```
started: bool
```

Return `True` once `start` has spawned the subprocess.

### started_time

```
started_time: str
```

Return the formatted timestamp captured when the test started.

### status

```
status: TestStatus
```

Return the current lifecycle status of the test.

### stderr

```
stderr: str | None
```

Return captured standard error once the test has finished.

### stdin

```
stdin: str | None
```

Return `None`; subclasses may override to expose stdin.

### stdout

```
stdout: str | None
```

Return captured standard output once the test has finished.

### suspended

```
suspended: bool
```

Return `True` if the subprocess is currently stopped.

### terminated

```
terminated: bool
```

Return `True` if the test ended due to termination signals.

### uid

```
uid: property = field(
    init=False,
    repr=True,
    default=property(lambda self: _get_uid(self)),
)
```

### accept

```
accept(v: Visitor[TestABC]) -> None
```

Accept a visit from a `Visitor`.

Source code in `src/socx/regression/test.py`

```
@override
def accept(self, v: Visitor[TestABC]) -> None:
    """Accept a visit from a `Visitor`."""
    v.visit(self)
```

### dref

```
dref(ref: int) -> UIDBase | None
```

Dereference a stored UID and return the tracked instance.

Source code in `src/socx/patterns/mixins/uid.py`

```
@classmethod
def dref(cls, ref: int) -> UIDBase | None:
    """Dereference a stored UID and return the tracked instance."""
    return UIDBase._get_inst(ref)
```

### interrupt

```
interrupt() -> None
```

Interrupt the execution of a running test with a SIGINT signal.

Source code in `src/socx/regression/test.py`

```
def interrupt(self) -> None:
    """Interrupt the execution of a running test with a SIGINT signal."""
    ...
```

### kill

```
kill() -> None
```

Kill the process with SIGKILL as a last resort.

Source code in `src/socx/regression/test.py`

```
@override
def kill(self) -> None:
    """Kill the process with SIGKILL as a last resort."""
    if self.running:
        self.process.kill()
```

### resume

```
resume() -> None
```

Resume the process if it is paused (sends a SIGCONT signal).

Source code in `src/socx/regression/test.py`

```
@override
def resume(self) -> None:
    """Resume the process if it is paused (sends a SIGCONT signal)."""
    if self.suspended:
        self.process.resume()
```

### start

```
start() -> None
```

Start a test in a subprocess.

Source code in `src/socx/regression/test.py`

```
@override
async def start(self) -> None:
    """Start a test in a subprocess."""
    if self.status not in (TestStatus.Idle, TestStatus.Pending):
        msg = "Cannot start a test when it is already running."
        exc = OSError(msg)
        logger.exception(msg, exc_info=exc, stack_info=True)
        raise exc

    self._status = TestStatus.Pending
    self._process = await asyncio.create_subprocess_shell(
        cmd=self.command.line, stdin=None, stdout=PIPE, stderr=PIPE
    )
    try:
        stdout, stderr = await self._process.communicate()
        self._status = TestStatus.Running
        self._started_time = time.time()

        while self.returncode is None:
            await asyncio.sleep(0)

        self._finished_time = time.time()
        self._stdout = stdout.decode()
        self._stderr = stderr.decode()
        self._status = TestStatus.Finished
    except Exception:
        self.terminate()
        self._status = TestStatus.Terminated
        self._result = TestResult.Failed
        raise

    if self.returncode == 0:
        self._result = self._parse_result()
    else:
        self._result = TestResult.Failed
```

### suspend

```
suspend() -> None
```

Send a SIGSTOP signal to suspend the test's running process.

Source code in `src/socx/regression/test.py`

```
@override
def suspend(self) -> None:
    """Send a SIGSTOP signal to suspend the test's running process."""
    if self.running:
        self.process.suspend()
```

### terminate

```
terminate() -> None
```

Terminate the process with SIGTERM.

Source code in `src/socx/regression/test.py`

```
@override
def terminate(self) -> None:
    """Terminate the process with SIGTERM."""
    if self.running:
        self.process.terminate()
```

### wait

```
wait(timeout: float | None = None) -> None
```

Wait for a test to terminate if it is running.

Source code in `src/socx/regression/test.py`

```
@override
def wait(self, timeout: float | None = None) -> None:
    """Wait for a test to terminate if it is running."""
    if self.running:
        self.process.wait()
```

## TestBase

```
TestBase(command: str | TestCommand, *args, **kwargs)
```

Provide common process-management behaviour for regression tests.

Methods:

- **`accept`** – Accept a visit from a Visitor.
- **`interrupt`** – Interrupt the execution of a running test with a SIGINT signal.
- **`kill`** – Interrupt the execution of a running test with a SIGKILL signal.
- **`resume`** – Resume the execution of a paused test.
- **`start`** – Start the execution of an idle test.
- **`suspend`** – Suspend the execution of a running test.
- **`terminate`** – Interrupt the execution of a running test with a SIGTERM signal.
- **`wait`** – Wait for a test to terminate if it is running.

Attributes:

- **`command`** (`TestCommand`) – Test execution command representation as an object.
- **`finished_time`** (`str`) – Return the formatted timestamp captured when the test finished.
- **`name`** (`str`) – Return the test's human readable name.
- **`pid`** (`int`) – Return the process identifier for the test's subprocess.
- **`result`** – Return the result enum once a test has completed.
- **`started_time`** (`str`) – Return the formatted timestamp captured when the test started.
- **`status`** (`TestStatus`) – Return the current lifecycle status of the test.

Source code in `src/socx/regression/test.py`

```
def __init__(self, command: str | TestCommand, *args, **kwargs) -> None:
    if isinstance(command, str):
        command = TestCommand(command)

    self._pid = os.getpid()
    self._name = "BASE"
    self._status = TestStatus.Idle
    self._result = TestResult.NA
    self._command = cast(TestCommand, command)
    self._process = None
    self._started_time = None
    self._finished_time = None
```

### command

```
command: TestCommand
```

Test execution command representation as an object.

### finished_time

```
finished_time: str
```

Return the formatted timestamp captured when the test finished.

### name

```
name: str
```

Return the test's human readable name.

### pid

```
pid: int
```

Return the process identifier for the test's subprocess.

### result

```
result
```

Return the result enum once a test has completed.

### started_time

```
started_time: str
```

Return the formatted timestamp captured when the test started.

### status

```
status: TestStatus
```

Return the current lifecycle status of the test.

### accept

```
accept(v: Visitor[TestABC]) -> None
```

Accept a visit from a `Visitor`.

Source code in `src/socx/regression/test.py`

```
@override
def accept(self, v: Visitor[TestABC]) -> None:
    """Accept a visit from a `Visitor`."""
    v.visit(self)
```

### interrupt

```
interrupt() -> None
```

Interrupt the execution of a running test with a SIGINT signal.

Source code in `src/socx/regression/test.py`

```
def interrupt(self) -> None:
    """Interrupt the execution of a running test with a SIGINT signal."""
    ...
```

### kill

```
kill() -> None
```

Interrupt the execution of a running test with a SIGKILL signal.

Source code in `src/socx/regression/test.py`

```
def kill(self) -> None:
    """Interrupt the execution of a running test with a SIGKILL signal."""
    ...
```

### resume

```
resume() -> None
```

Resume the execution of a paused test.

Source code in `src/socx/regression/test.py`

```
def resume(self) -> None:
    """Resume the execution of a paused test."""
    ...
```

### start

```
start() -> None
```

Start the execution of an idle test.

Source code in `src/socx/regression/test.py`

```
async def start(self) -> None:
    """Start the execution of an idle test."""
    ...
```

### suspend

```
suspend() -> None
```

Suspend the execution of a running test.

Source code in `src/socx/regression/test.py`

```
def suspend(self) -> None:
    """Suspend the execution of a running test."""
    ...
```

### terminate

```
terminate() -> None
```

Interrupt the execution of a running test with a SIGTERM signal.

Source code in `src/socx/regression/test.py`

```
def terminate(self) -> None:
    """Interrupt the execution of a running test with a SIGTERM signal."""
    ...
```

### wait

```
wait(timeout: float | None = None) -> None
```

Wait for a test to terminate if it is running.

Source code in `src/socx/regression/test.py`

```
def wait(self, timeout: float | None = None) -> None:
    """Wait for a test to terminate if it is running."""
    ...
```

## TestCommand

```
TestCommand(line: str | TestCommand)
```

Represent a test invocation parsed from a command-line string.

Methods:

- **`dref`** – Dereference a stored UID and return the tracked instance.
- **`extract_argv`** – Return the value that follows the requested CLI argument.

Attributes:

- **`arguments`** (`tuple[str, ...]`) –
- **`escaped`** (`str`) –
- **`line`** (`str`) –
- **`name`** (`str`) –
- **`ref`** (`int`) – Return the object's assigned unique identifier.
- **`uid`** (`property`) –

Source code in `src/socx/regression/test.py`

```
def __init__(self, line: str | TestCommand) -> None:
    if isinstance(line, TestCommand):
        self = line
        return

    self.line = line
    self.arguments = tuple(arg.strip() for arg in self.line.split())
    self.name = self.arguments[0] if self.arguments else ""
    self.escaped = shlex.quote(self.line)
```

### arguments

```
arguments: tuple[str, ...] = tuple(
    (strip()) for arg in (split())
)
```

### escaped

```
escaped: str = quote(line)
```

### line

```
line: str = line
```

### name

```
name: str = arguments[0] if arguments else ''
```

### ref

```
ref: int
```

Return the object's assigned unique identifier.

### uid

```
uid: property = field(
    init=False,
    repr=True,
    default=property(lambda self: _get_uid(self)),
)
```

### dref

```
dref(ref: int) -> UIDBase | None
```

Dereference a stored UID and return the tracked instance.

Source code in `src/socx/patterns/mixins/uid.py`

```
@classmethod
def dref(cls, ref: int) -> UIDBase | None:
    """Dereference a stored UID and return the tracked instance."""
    return UIDBase._get_inst(ref)
```

### extract_argv

```
extract_argv(arg: str) -> str | None
```

Return the value that follows the requested CLI argument.

Source code in `src/socx/regression/test.py`

```
def extract_argv(self, arg: str) -> str | None:
    """Return the value that follows the requested CLI argument."""
    for i, attr in enumerate(self.arguments):
        if attr.startswith("--") or attr.startswith("-"):
            if attr == arg and i + 1 < len(self.arguments):
                return self.arguments[i + 1]
            if attr.removeprefix("-") == arg and i + 1 < len(
                self.arguments
            ):
                return self.arguments[i + 1]
            if attr.removeprefix("--") == arg and i + 1 < len(
                self.arguments
            ):
                return self.arguments[i + 1]
    return None
```

## TestResult

Represents the result of a test that had finished and exited normally.

#### Members

Na

TestResult Test has not yet finished running and therefore result is non-applicable.

TestResult

Test had finished and terminated normally with no errors and a 0 exit code.

TestResult

Test had finished either normally or abnormally with a non-zero exit code.

Attributes:

- **`Failed`** –
- **`NA`** –
- **`Passed`** –

### Failed

```
Failed = auto()
```

### NA

```
NA = auto()
```

### Passed

```
Passed = auto()
```

## TestStatus

TestStatus representation of a test process as an `IntEnum`.

#### Members

Idle: IntEnum Idle, waiting to be scheduled for execution.

IntEnum

Test is scheduled for execution in an active session.

IntEnum

Test is currently running.

IntEnum

Test has been stopped intentionally.

IntEnum

Test had finished running normally with an exit code 0.

IntEnum

Test was intentionally terminated by a signal.

Attributes:

- **`Finished`** –
- **`Idle`** –
- **`Pending`** –
- **`Running`** –
- **`Stopped`** –
- **`Terminated`** –

### Finished

```
Finished = auto()
```

### Idle

```
Idle = 0
```

### Pending

```
Pending = auto()
```

### Running

```
Running = auto()
```

### Stopped

```
Stopped = auto()
```

### Terminated

```
Terminated = auto()
```

## TopDownTraversal

Pre-order traversal that visits parents before descendants.

Methods:

- **`accept`** – Visit n before recursively traversing its children.

### accept

```
accept(
    n: NODE, v: Visitor[NODE], p: Structure[NODE]
) -> None
```

Visit `n` before recursively traversing its children.

Source code in `src/socx/patterns/visitor/traversal.py`

```
@classmethod
def accept(cls, n: NODE, v: Visitor[NODE], p: Structure[NODE]) -> None:
    """Visit ``n`` before recursively traversing its children."""
    v.visit(n)

    for c in p.children(n):
        cls.accept(c, v, p)
```

## Traversal

Adapter interface that controls how nodes accept visitors.

Methods:

- **`accept`** – Accept visits of a NODE n from a Visitor v.

### accept

```
accept(
    n: NODE, v: Visitor[NODE], p: Structure[NODE]
) -> None
```

Accept visits of a `NODE` n from a `Visitor` v.

Source code in `src/socx/patterns/visitor/protocol.py`

```
@classmethod
def accept(cls, n: NODE, v: Visitor[NODE], p: Structure[NODE]) -> None:
    """Accept visits of a `NODE` n from a `Visitor` v."""
    ...
```

## TreeFormatter

Format Dynaconf settings into an inspectable tree view.

## UIDMixin

```
UIDMixin()
```

Unique instance ID mixin class.

Extending this class assigns a unique instance id to all instances of the extending subclass.

Methods:

- **`dref`** – Dereference a stored UID and return the tracked instance.

Attributes:

- **`ref`** (`int`) – Return the object's assigned unique identifier.
- **`uid`** (`property`) –

### ref

```
ref: int
```

Return the object's assigned unique identifier.

### uid

```
uid: property = field(
    init=False,
    repr=True,
    default=property(lambda self: _get_uid(self)),
)
```

### dref

```
dref(ref: int) -> UIDBase | None
```

Dereference a stored UID and return the tracked instance.

Source code in `src/socx/patterns/mixins/uid.py`

```
@classmethod
def dref(cls, ref: int) -> UIDBase | None:
    """Dereference a stored UID and return the tracked instance."""
    return UIDBase._get_inst(ref)
```

## Visitor

Protocol describing objects that can visit nodes.

Methods:

- **`visit`** – Visit a node of a structure.

### visit

```
visit(n: NODE) -> None
```

Visit a node of a structure.

Source code in `src/socx/patterns/visitor/protocol.py`

```
def visit(self, n: NODE) -> None:
    """Visit a node of a structure."""
    ...
```

## add_converters

```
add_converters(converters: Iterable[Converter]) -> None
```

Register converters with Dynaconf using their inferred names.

Source code in `src/socx/config/converters.py`

```
def add_converters(converters: Iterable[Converter]) -> None:
    """Register converters with Dynaconf using their inferred names."""
    for converter in converters:
        add_converter(converter.name, converter)
```

## add_filter

```
add_filter(filter: Filter) -> None
```

Attach a filter to the module-level logger.

Source code in `src/socx/io/log.py`

```
def add_filter(filter: logging.Filter) -> None:  # noqa: A002
    """Attach a filter to the module-level logger."""
    logger.addFilter(filter)
```

## add_handler

```
add_handler(handler: Handler) -> None
```

Attach `handler` to the module-level logger.

Source code in `src/socx/io/log.py`

```
def add_handler(handler: logging.Handler) -> None:
    """Attach ``handler`` to the module-level logger."""
    logger.addHandler(handler)
```

## add_options

```
add_options(*options: Any) -> Decorator[AnyCallable]
```

Compose multiple option decorators into a single decorator.

Source code in `src/socx/cli/options.py`

```
def add_options(*options: Any) -> Decorator[AnyCallable]:
    """Compose multiple option decorators into a single decorator."""

    def _add_options(func):
        for opt in reversed(options):
            func = opt(func)
        return func

    return _add_options
```

## get_converters

```
get_converters() -> Iterable[tuple[str, Converter]]
```

Yield converter registrations, wrapping raw callables as needed.

Source code in `src/socx/config/converters.py`

```
def get_converters() -> Iterable[tuple[str, Converter]]:
    """Yield converter registrations, wrapping raw callables as needed."""
    from dynaconf.utils.parse_conf import converters

    rv = []
    for name, cvt in converters.items():
        if not isinstance(cvt, Converter):
            cvt = GenericConverter(name, cvt)
        rv.append((name, cvt))
    return rv
```

## get_handler

```
get_handler(name: str) -> Handler | None
```

Return a handler registered under `name` if one exists.

Source code in `src/socx/io/log.py`

```
def get_handler(name: str) -> logging.Handler | None:
    """Return a handler registered under ``name`` if one exists."""
    return logging.getHandlerByName(name)
```

## get_handler_names

```
get_handler_names() -> Iterable[str]
```

Return the names of all registered logging handlers.

Source code in `src/socx/io/log.py`

```
def get_handler_names() -> Iterable[str]:
    """Return the names of all registered logging handlers."""
    return logging.getHandlerNames()
```

## get_level

```
get_level(logger_: Logger) -> Level
```

Return the effective log level for `logger_` as a `Level` enum.

Source code in `src/socx/io/log.py`

```
def get_level(logger_: logging.Logger) -> Level:
    """Return the effective log level for ``logger_`` as a ``Level`` enum."""
    return Level(logger_.getEffectiveLevel())
```

## get_logger

```
get_logger(
    name: str, filename: str | None = None
) -> Logger
```

Return a child logger configured with optional file output.

Source code in `src/socx/io/log.py`

```
def get_logger(name: str, filename: str | None = None) -> logging.Logger:
    """Return a child logger configured with optional file output."""
    rv = logger.getChild(name)
    if filename is not None:
        handler = _get_file_handler(filename)
        handler.setFormatter(DEFAULT_CHILD_FORMATTER)
        rv.addHandler(handler)
    return rv
```

## global_options

```
global_options() -> Callable[..., Decorator[AnyCallable]]
```

Apply the standard set of global SoCX CLI options.

Source code in `src/socx/cli/options.py`

```
def global_options() -> Callable[..., Decorator[AnyCallable]]:
    """Apply the standard set of global SoCX CLI options."""
    return add_options(debug, configure, verbosity)
```

## has_handlers

```
has_handlers() -> bool
```

Return `True` if the module-level logger has active handlers.

Source code in `src/socx/io/log.py`

```
def has_handlers() -> bool:
    """Return ``True`` if the module-level logger has active handlers."""
    return logger.hasHandlers()
```

## is_enabled_for

```
is_enabled_for(level: Level) -> bool
```

Return `True` if the module-level logger handles `level`.

Source code in `src/socx/io/log.py`

```
def is_enabled_for(level: Level) -> bool:
    """Return ``True`` if the module-level logger handles ``level``."""
    if isinstance(level, str):
        level = logging.getLevelName(level)
    return logger.isEnabledFor(level)
```

## log_it

```
log_it(
    level: str | int = DEBUG, logger: Logger | None = None
) -> Callable[[AnyCallable], AnyCallable]
```

Add automatic entered/returned logging to decorated callables.

Source code in `src/socx/io/decorators.py`

```
def log_it(
    level: str | int = logging.DEBUG,
    logger: logging.Logger | None = None,
) -> Callable[[AnyCallable], AnyCallable]:
    """Add automatic entered/returned logging to decorated callables."""
    if isinstance(level, str):
        level_map: dict[str, int] = logging.getLevelNamesMapping()
        level = level_map[level]

    if logger is None:
        logger = logging.getLogger("socx-cli")

    def _log_it(f: AnyCallable) -> AnyCallable:
        sig = f"{f.__name__}{signature(f)}"

        @wraps(f)
        def wrapper(*args, **kwargs):
            logger.log(level, f"[{sig}] entered.")
            rv = f(*args, **kwargs)
            logger.log(level, f"[{sig}] returned {rv}.")
            return rv

        return wrapper

    return _log_it
```

## remove_filter

```
remove_filter(filter: Filter) -> None
```

Detach a filter from the module-level logger.

Source code in `src/socx/io/log.py`

```
def remove_filter(filter: logging.Filter) -> None:  # noqa: A002
    """Detach a filter from the module-level logger."""
    logger.removeFilter(filter)
```

## remove_handler

```
remove_handler(handler: Handler) -> None
```

Remove `handler` from the module-level logger.

Source code in `src/socx/io/log.py`

```
def remove_handler(handler: logging.Handler) -> None:
    """Remove ``handler`` from the module-level logger."""
    logger.removeHandler(handler)
```

## set_level

```
set_level(
    level: Level, logger_: Logger | None = None
) -> None
```

Set the log level on the provided logger (defaults to module logger).

Source code in `src/socx/io/log.py`

```
def set_level(level: Level, logger_: logging.Logger | None = None) -> None:
    """Set the log level on the provided logger (defaults to module logger)."""
    target = logger_ or logger
    target.setLevel(level)
```

## validate_all

```
validate_all(
    settings: LazySettings, register: bool = False
) -> None
```

Run validation against all registered validators.

Source code in `src/socx/config/validators.py`

```
def validate_all(settings: LazySettings, register: bool = False) -> None:
    """Run validation against all registered validators."""
    if register:
        settings.validators.register(get_validators(settings))

    settings.validators.validate_all()
```
