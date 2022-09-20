def get_greeting(name: str) -> str:
    print(f'Hello {name}')
get_greeting(input())

if __name__ == "__main__":
    message = get_greeting("World")
    print(message)
