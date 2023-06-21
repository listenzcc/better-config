# 让 Python 更好用，OmegaConf

问：写一套好用的程序分几部？

答：分三步！第一步是功能抽象，第二步是为功能配置参数，第三步是让这些参数跑起来。

感谢 OmegaConf 提供的配置项解决方案，它能够让第二步走得更加容易。

本文的详细说明可见我的 Github 文档库

[https://github.com/listenzcc/better-config.git](https://github.com/listenzcc/better-config.git)

---
- [让 Python 更好用，OmegaConf](#让-python-更好用omegaconf)
  - [令人烦躁的配置项](#令人烦躁的配置项)
  - [何为 OmegaConf](#何为-omegaconf)
  - [类型安全](#类型安全)
  - [参数灵活性](#参数灵活性)


## 令人烦躁的配置项

在软件配置中的一些复杂或难以处理的参数选项。这些参数可能涉及到多层嵌套、大量的选项或需要复杂的处理逻辑。这样的参数项可能会给配置管理带来一些挑战，导致配置文件难以理解、维护困难或容易出错。典型情况有

1. 多层嵌套：当配置具有深层嵌套结构时，访问和修改特定参数项可能变得困难。这可能导致代码中的混乱和错误。
2. 大量选项：如果配置中有大量的选项，手动管理和更新这些选项可能会变得繁琐。此外，当需要添加新选项或删除旧选项时，修改配置可能变得复杂。
3. 复杂的依赖关系：某些参数项可能依赖于其他参数项的值或状态。当存在复杂的依赖关系时，确保参数项的一致性和正确性可能会变得复杂。
4. 不一致的命名约定：如果配置中的参数项命名不一致或缺乏清晰的约定，阅读和理解配置文件可能会变得困难。这可能导致开发人员难以找到特定参数项或正确理解其含义。

为了解决这些问题，我们需要**一种高效的配置项管理系统**，支持灵活的配置组织和访问方式，我们希望它**能够提供一致的API**，无论配置是如何创建的，都可以使用相同的方式进行访问。此外，它最好还能**提供类型安全的功能**，帮助减少配置错误并提供更好的代码提示和类型检查。这些功能可以帮助简化配置管理，减少令人烦躁的参数项带来的困扰。

## 何为 OmegaConf

OmegaConf 是一个Python库，用于管理和组织配置信息。它提供了一个灵活的配置系统，支持使用YAML格式定义配置，并支持从多个来源（例如文件、命令行参数、环境变量）合并配置。OmegaConf 还提供了一个一致的API，无论配置是如何创建的，都可以使用相同的方式访问配置项。

OmegaConf 的一个重要特性是支持分层配置。这意味着你可以将配置分为多个层级，并在不同的层级中定义不同的配置项。这样可以方便地覆盖和继承配置，使配置管理更加灵活和可扩展。

另外，OmegaConf 还提供了结构化配置（Structured Configs）的功能，可以在配置中定义和强制类型，以提供运行时的类型安全性。这可以帮助减少配置错误，并提供更好的代码提示和类型检查。

总之，OmegaConf 是一个功能强大的配置管理库，旨在简化配置的组织、合并和访问，并提供运行时的类型安全性。它广泛用于各种Python项目中，特别是在涉及复杂配置和多环境管理的情况下，它的功能显得尤其好用。

> OmegaConf is a YAML based hierarchical configuration system, with support for merging configurations from multiple sources (files, CLI argument, environment variables) providing a consistent API regardless of how the configuration was created. OmegaConf also offers runtime type safety via Structured Configs.
> 

[OmegaConf — OmegaConf 2.3.0 documentation](https://omegaconf.readthedocs.io/en/2.3_branch/index.html)

## 类型安全

类型安全是指在编程语言中，在编译时或运行时能够检测和防止不符合预期类型的操作或赋值。它旨在减少类型相关的错误，并提供更可靠的代码。在配置管理中，类型安全是指能够在配置文件中定义和强制类型，以确保配置项具有预期的数据类型。这有助于减少由于错误的类型赋值或操作而引起的问题。

OmegaConf 提供了运行时类型安全的功能，称为结构化配置（Structured Configs）。使用结构化配置，可以在配置中明确定义参数项的数据类型，并在运行时对其进行验证。这样可以确保配置项在被访问或修改时具有正确的类型，并避免潜在的类型错误。

```python
# Create omega conf with type safty with structured configs

class LoggingLevel(Enum):
    INFO = logging.INFO
    DEBUG = logging.DEBUG
    ERROR = logging.ERROR
    FATAL = logging.FATAL
    WARNING = logging.WARNING
    CRITICAL = logging.CRITICAL

@dataclass
class LocalServer:
    local: str = '0.0.0.0'
    port: int = 7788
    coding: str = 'utf-8'
    chroot: Path = Path('D:\\')
    mode: Mode = Mode.unknown
    loggingLevel: LoggingLevel = LoggingLevel.DEBUG

OmegaConf.create(LocalServer)
```

## 参数灵活性

在实际使用场景中，我们往往需要灵活地改变某些配置参数。灵活性可以使我们根据不同的需求或环境进行配置调整，而无需修改源代码或重新部署应用程序。OmegaConf 提供了一些功能来增强配置参数的灵活性：

1. 多来源的配置合并：OmegaConf 允许从多个来源（例如文件、命令行参数、环境变量）读取配置，并将它们合并成一个一致的配置对象。这意味着你可以在不同的地方定义和修改配置参数，而不必依赖于单一的配置文件。
2. 参数覆盖和继承：OmegaConf 支持参数的覆盖和继承。你可以通过在较高层级的配置中重新定义特定参数，覆盖之前的取值。这使得在不同环境或使用情况下修改参数变得非常方便。
3. 运行时修改：OmegaConf 允许在运行时动态地修改配置参数。你可以通过编程方式访问和修改配置项，根据需要进行动态调整。这样，你可以根据运行时条件或用户输入来更改参数，以满足不同的需求。

通过这些功能，OmegaConf 提供了一种灵活的配置管理方式，使你能够在不同的场景下灵活地更改配置参数。无需修改源代码或重新部署应用程序，你可以通过配置文件、命令行参数、环境变量或运行时修改等方式轻松调整配置，以适应不同的需求和环境。

以下是通过“命令行参数”进行修改的样例，用户可以通过这种方式使软件在启动时读入临时参数。

```python
# Merge conf with the user input
# $ python .\config\defines.py local_server.port=2222 other.setup=cli

oc = OmegaConf.create(dict(
    local_server=LocalServer
))
print('\nDefault:\n', oc)

cli_oc = OmegaConf.from_cli(sys.argv[1:])
print('\nCli:\n', cli_oc)

merged_oc = OmegaConf.merge(oc, cli_oc)
print('\nMerged:\n', merged_oc)
print()
```

![Untitled](%E8%AE%A9%20Python%20%E6%9B%B4%E5%A5%BD%E7%94%A8%EF%BC%8COmegaConf%20f76bdfc5dadd491cb4955524db67b177/Untitled.png)