from calc.commands.add import AddCommand
from calc.plugin_loader import load_plugins
from calc.history import HistoryManager
from calc.logger import logger

def main():
    history = HistoryManager()
    plugins = load_plugins()

    while True:
        command = input(">> ").strip()

        if command == "exit":
            break

        elif command.startswith("add"):
            try:
                _, a, b = command.split()
                result = AddCommand().execute(a, b)
                print(f"Result: {result}")
                history.add_record(command, result)
                logger.info(f"Executed {command} with result {result}")
            except Exception as e:
                print(f"Error: {e}")
                logger.error(f"Failed to execute {command}: {e}")

        elif command == "history":
            history.show_history()

        elif command == "clear":
            history.clear_history()
            print("History cleared.")
            logger.info("Cleared history.")

        elif command.startswith("plugin"):
            try:
                parts = command.split()
                name = parts[1]
                args = parts[2:]
                if name in plugins:
                    result = plugins[name].run(*args)
                    print(f"Plugin Result: {result}")
                    history.add_record(command, result)
                    logger.info(f"Executed plugin {command} with result {result}")
                else:
                    print("Plugin not found.")
                    logger.warning(f"Plugin '{name}' not found.")
            except Exception as e:
                print(f"Error: {e}")
                logger.error(f"Plugin execution error for '{command}': {e}")

        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()

