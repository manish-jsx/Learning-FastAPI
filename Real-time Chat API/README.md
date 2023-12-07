
# Real-time Chat API with FastAPI and WebSockets

This is a simple example of a real-time chat API using FastAPI and WebSockets. Users can join different chat rooms, send, and receive messages. The API also includes a basic authentication mechanism.

## Features

- Real-time communication using WebSockets
- User authentication for joining chat rooms
- Simple room management
- Basic message broadcasting

## Prerequisites

Make sure you have Python and pip installed on your machine.

```bash
pip install -r requirements.txt
```

## Setup

1. Clone the repository:

```bash
git clone https://github.com/your-username/real-time-chat-api.git
cd real-time-chat-api
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the FastAPI application:

```bash
uvicorn main:app --reload
```

2. Open your browser and visit [http://localhost:8000/](http://localhost:8000/) to interact with the chat interface.

## API Endpoints

- WebSocket Endpoint: `ws://localhost:8000/ws/{room_id}/{user_id}`
  - `{room_id}`: The ID of the chat room
  - `{user_id}`: The ID of the user

## Authentication

- Use the `X-API-Key` header for authentication when connecting to the WebSocket endpoint.
- For simplicity, the example uses predefined API keys (`user1`, `key1`, etc.).

## Customization

Feel free to customize the code to meet your specific requirements. You can add more features such as:

- Advanced authentication mechanisms
- Room management with creation and deletion
- Message persistence
- User management

## Contributing

If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request.

Happy chatting!
```

