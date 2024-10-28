1. Add a security layer based on JWT tokens. An authentication module may be added if the app will use a database
2. Enhance performances by using a task queue instead of a mutex lock **if the app is to be kept lightweight and not use a DB**
3. Use an in-memory database for high performances, scalability and less code problems to handle. The changes should be applied in StackManger and Stack classes and the Factory design pattern will be fully applied.
4. ADD logging for operations (may be asynchronous  for better performance)
5. Since we have logs we can do the app monitoring
5. ADD health check endpoints
6. Containerize the app for easier deployments 