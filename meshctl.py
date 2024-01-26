#! /usr/bin/python3
import argparse
from lib.Docker import Docker  # Assuming your Docker class is in a different module

def main():
    parser = argparse.ArgumentParser(description="DOCKER CONTAINER MANAGER")
    parser.add_argument("name", help="Name of the Docker container")

    subparsers = parser.add_subparsers(dest="command", help="Subcommands")

    # Subparser for the 'run' command
    run_parser = subparsers.add_parser("run", help="Spawn a Mesh container")

    # Subparser for the 'logs' command
    subparsers.add_parser("logs", help="Get logs of a Mesh container")

    # Subparser for the 'stop' command
    stop_parser = subparsers.add_parser("stop_remove", help="Stop and remove a Mesh container")

    # Subparser for the 'create_user' command
    subparsers.add_parser("wg_ip", help="Create a user inside the Mesh container")

    # Subparser for the 'getIP' command
    subparsers.add_parser("getIP", help="Get IP information of Mesh containers")

    args = parser.parse_args()

    docker_manager = Docker(args.name)

    if args.command == "run":
        docker_manager.run_image()
        docker_manager.create_user()
        docker_manager.get_wireguard_ip()
    elif args.command == "logs":
        logs = docker_manager.get_container_logs()
        print(logs)
    elif args.command == "stop_remove":
        docker_manager.stop_and_remove()
    elif args.command == "wg_ip":
        docker_manager.get_wireguard_ip()
    elif args.command == "getIP":
        docker_manager.getIP()

if __name__ == "__main__":
    main()
