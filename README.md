This api allows you to stream deriv price data for any instrument live, it saves to memcache using Redis, which can be used for further operations by connecting to the redis stream from another container or process.
- To Run api, make sure docker is installed.
- use command `docker compose up -d` to run the stack from the project root directory.
