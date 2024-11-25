import socket
import time  # Import time for sleep
from colorama import Fore, Style, init
import sys  # For sys.exit

# Initialize colorama for cross-platform compatibility
init()

def print_instructions():
    """Display usage instructions."""
    print(f"""
{Fore.RED}
      ______
   .-        -.
  /            \\
 |,  .-.  .-.  ,|
 | )(_o/  \o_)( |
 |/     /\\     \\|
 (_     ^^     _)
  \\__|IIIIII|__/
   | \\IIIIII/ |
   \\          /
    `--------`
{Style.RESET_ALL}
""")
    print(f"{Fore.RED}Designed & Written by pxzvc{Style.RESET_ALL}")
    print()
    print(f"{Fore.CYAN}Usage:{Style.RESET_ALL}")
    print()
    print(f"  portping -p <port> <host>")
    print()
    print(f"{Fore.CYAN}Example:{Style.RESET_ALL}")
    print()
    print(f"  portping -p 80 google.com\n")

def ping_port(host, port):
    """Attempts to connect to the specified host and port."""
    try:
        start_time = time.time()  # Record the start time
        with socket.create_connection((host, port)) as sock:
            end_time = time.time()  # Record the end time
            elapsed_time = (end_time - start_time) * 1000  # Convert to milliseconds
            print(f"{Fore.GREEN}Connected{Style.RESET_ALL} to {host} on port {port} in {elapsed_time:.2f}ms")
    except socket.timeout:
        print(f"{Fore.RED}Connection to {host} on port {port} timed out{Style.RESET_ALL}")
    except socket.gaierror:
        print(f"{Fore.YELLOW}Failed to resolve hostname {host}{Style.RESET_ALL}")
    except ConnectionRefusedError:
        print(f"{Fore.RED}Connection refused by {host} on port {port}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.YELLOW}Failed to connect to {host}:{port}: {e}{Style.RESET_ALL}")

def main():
    print_instructions()  # Show instructions only once

    while True:
        try:
            # Interactive input for commands
            command = input(f"{Fore.CYAN}portping> {Style.RESET_ALL}").strip()
            if command.lower() in ["exit", "quit"]:
                print(f"{Fore.YELLOW}Exiting...{Style.RESET_ALL}")
                sys.exit(0)

            # Parse command
            if command.startswith("portping"):
                parts = command.split()
                if "-p" in parts:
                    port_index = parts.index("-p") + 1
                    try:
                        port = int(parts[port_index])
                        host = parts[-1]

                        # Infinite ping loop for the specified host and port
                        print()
                        print(f"{Fore.YELLOW}Starting ping to {host} on port {port}. Press Ctrl+C to stop.{Style.RESET_ALL}")
                        print()
                        while True:
                            try:
                                ping_port(host, port)
                                time.sleep(1)  # Add a 1-second delay between pings
                            except KeyboardInterrupt:
                                print(f"\n{Fore.YELLOW}Ping stopped. Returning to command line...{Style.RESET_ALL}")
                                print()
                                break

                    except (ValueError, IndexError):
                        print(f"{Fore.RED}Invalid command. Usage: portping -p <port> <host>{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}Missing -p <port>. Usage: portping -p <port> <host>{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Unknown command. Type 'portping -p <port> <host>' or 'exit' to quit.{Style.RESET_ALL}")

        except KeyboardInterrupt:
            # Handle Ctrl+C without exiting
            print(f"\n{Fore.YELLOW}Ctrl+C detected. Type 'exit' to quit or enter a new command.{Style.RESET_ALL}")


if __name__ == "__main__":
    main()
