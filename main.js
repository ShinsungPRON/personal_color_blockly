function run() {
    let socket = new WebSocket(
        "ws://localhost:8080"
    )
    socket.send("a")
    socket.close()
}