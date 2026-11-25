[English](README.md) | **简体中文**

# YouTube 字幕（文字稿）API

获取任意 YouTube 视频的字幕文本，可按带时间戳的片段或纯文本返回，并可指定语言。

由 [Serpent API](https://apiserpent.com) 提供。完整文档：**[YouTube Transcript API 文档](https://apiserpent.com/youtube-transcript-api)**。

## 快速开始

1. 在 [apiserpent.com](https://apiserpent.com) 注册并获取 API Key，每个账号赠送 10 次免费调用。
2. 在请求头 `X-API-Key` 中带上你的 Key 调用接口：

```bash
curl -G "https://apiserpent.com/api/social/youtube/transcript" \
  --data-urlencode "video=https://youtu.be/8jPQjjsBbIc" \
  --data-urlencode "output=text" \
  -H "X-API-Key: $SERPENT_API_KEY"
```

## 接口

`GET https://apiserpent.com/api/social/youtube/transcript`

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| `video` | 是 | 11 位视频 id 或任意 YouTube 链接（watch、`youtu.be`、Shorts、embed、live） |
| `lang` | 否 | 语言代码，如 `en`、`de`、`pt-BR`；不传则使用视频的主要语言。 |
| `output` | 否 | `segments`（默认）或 `text` |

## 返回结果

字段：`video_id`、`title`、`channel`、`duration_seconds`、`language`、`is_auto_generated`、`available_languages[]`、`segments[]`（`start`、`duration`、`text`）、`text`。

完整字段列表和响应示例请参阅[文档](https://apiserpent.com/youtube-transcript-api)。

## 示例代码

| 文件 | 语言 | 运行方式 |
| --- | --- | --- |
| [`example.py`](example.py) | Python 3（`pip install requests`） | `SERPENT_API_KEY=sk_live_... python example.py` |
| [`example.mjs`](example.mjs) | Node.js 18+（无需依赖） | `SERPENT_API_KEY=sk_live_... node example.mjs` |

## 应用场景

- 用大模型做视频摘要
- 基于视频内容的搜索与 RAG
- 字幕制作与内容二次创作

## Serpent API 的更多能力

- [Serpent API 文档](https://apiserpent.com/docs)：Google、Bing、Yahoo、DuckDuckGo 和 Brave 搜索结果，以及 AI 引用排名跟踪
- [GitHub 上的全部 SDK 与工具](https://github.com/apiserpent)

## 许可证

MIT
