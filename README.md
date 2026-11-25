**English** | [简体中文](README.zh-CN.md)

# YouTube Transcript API

Get the transcript of any YouTube video as timed segments or plain text, in the language you choose.

Powered by [Serpent API](https://apiserpent.com). Full reference: **[YouTube Transcript API docs](https://apiserpent.com/youtube-transcript-api)**.

## Quick start

1. Get an API key at [apiserpent.com](https://apiserpent.com). Every account starts with 10 free API calls.
2. Call the endpoint with your key in the `X-API-Key` header:

```bash
curl -G "https://apiserpent.com/api/social/youtube/transcript" \
  --data-urlencode "video=https://youtu.be/8jPQjjsBbIc" \
  --data-urlencode "output=text" \
  -H "X-API-Key: $SERPENT_API_KEY"
```

## Endpoint

`GET https://apiserpent.com/api/social/youtube/transcript`

| Parameter | Required | Description |
| --- | --- | --- |
| `video` | Yes | 11-character video id or any YouTube link (watch, `youtu.be`, Shorts, embed, live) |
| `lang` | No | Language code such as `en`, `de`, `pt-BR`. Omit for the video's main language. |
| `output` | No | `segments` (default) or `text` |

## Response

`video_id`, `title`, `channel`, `duration_seconds`, `language`, `is_auto_generated`, `available_languages[]`, `segments[]` (`start`, `duration`, `text`), `text`.

See the [docs](https://apiserpent.com/youtube-transcript-api) for the complete field list and sample responses.

## Examples

| File | Language | Run |
| --- | --- | --- |
| [`example.py`](example.py) | Python 3 (`pip install requests`) | `SERPENT_API_KEY=sk_live_... python example.py` |
| [`example.mjs`](example.mjs) | Node.js 18+ (no dependencies) | `SERPENT_API_KEY=sk_live_... node example.mjs` |

## Use cases

- Video summarisation with LLMs
- Search and RAG over video content
- Subtitles, captions and content repurposing

## More from Serpent API

- [Serpent API docs](https://apiserpent.com/docs) - Google, Bing, Yahoo, DuckDuckGo and Brave search, plus AI rank tracking
- [All SDKs and tools on GitHub](https://github.com/apiserpent)

## License

MIT
