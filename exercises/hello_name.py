import sys
from select import poll
from utime import sleep

poll_obj = poll()
# Register sys.stdin (standard input) for monitoring read events with priority 1
poll_obj.register(sys.stdin, 1)


def main():

    print("Please enter your name: ")
    while True:
        try:
            # update vector values IFF poll object has anything to say
            if poll_obj.poll(10):
                print("something arrived in the poll object")
                input_str = sys.stdin.readline().rstrip()
                print(f"Hello, {input_str}!")
                # Quit after saying hello
                break

            sleep(0.1)
        except KeyboardInterrupt:
            break

    print("Finished.")


if __name__ == "__main__":
    main()
