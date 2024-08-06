# Healthcheck

## Install the "jq" command

```jq``` takes an input JSON stream and reformats it to have color syntax highlighting and indentation.

```sh
brew install jq
```

## Shell command to monitor health

```sh
curl -s http://dans-macbook-pro.local:14240/api/ping | jq
```

## Sample Response

```json
{
  "error": false,
  "message": "pong",
  "results": null
}
```

## Testing Builtin Endpoints

```sh
curl -s http://dans-macbook-pro.local:9000/endpoints/got | jq
```

This will return about 2100 lines of JSON.

## Testing Specific Query

```sh
curl -s http://dans-macbook-pro.local:14240/restpp/query/got/countPeople2 | jq
```

This returns:

```json
{
  "version": {
    "edition": "enterprise",
    "api": "v2",
    "schema": 3
  },
  "error": false,
  "message": "",
  "results": [
    {
      "Results.size()": 187
    }
  ]
}
```