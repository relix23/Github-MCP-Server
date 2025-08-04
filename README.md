# 🧠 GitHub MCP Server

A lightweight [Model Context Protocol (MCP)](https://modelcontextprotocol.io/overview) server built with [FastMCP](https://github.com/jlowin/fastmcp) to expose and automate **GitHub operations** using LLM-compatible tools.

---

## ✨ Features

- ⚙️ GitHub API integration via MCP tools
- 🤖 LLM-friendly schema for interaction with AI agents
- 🔐 Optional authentication support
- 🧩 Easy to extend with new GitHub operations

---

## 🔧 Supported GitHub Operations

This server currently supports the following GitHub features as callable MCP tools:

| Tool Name                                    | Description                                                                       |
|----------------------------------------------|-----------------------------------------------------------------------------------|
| `get_user_bio`                               | Retrieve bio of a user                                                            |
| `get_github_files`                           | Recursively fetch all files and directories from a GitHub repo starting at 'path' |
| `get_file_content`                           | Fetches the content of a file from a GitHub repository.                           |
| `create_pull_request_with_branch`            | Creates a new branch and then a pull request on GitHub                            |
| `create_github_issue`                        | Creates an issue on a GitHub repository                                           |

> ✅ More tools can be added easily by decorating a Python function with `@mcp.tool()`.

---

## 🚀 Quickstart

1. **Clone the repository:**

   ```bash
   git clone https://github.com/mymadhavyadav07/Github-MCP-server.git
   cd Github-MCP-Server

2. **Install dependencies:**

   Using [`uv`](https://github.com/astral-sh/uv) (recommended for Python 3.11+):

   ```bash
   uv venv
   uv pip install -r requirements.txt

3. **Configure Github Access Token:**
   - Create a **.env** file and copy contents from **.env.example** to **.env**
   - Replace **GITHUB_TOKEN** with your own Github Access Token. You can generate one from [here](https://github.com/settings/tokens)
   ```bash
   GITHUB_TOKEN = "<GITHUB_TOKEN>"
   ```
   

5. **Download and install Claude Desktop** - [Claude Desktop](https://claude.ai/download)

6. **Install MCP Server in Claude:**  
   - Activate Virtual Environment:  
   ```bash
   .venv\Scripts\activate
   ```

   - Now, finally install the MCP Server in Claude:  
   ```bash
   uv run mcp install main.py
   ```

7. **Now you are all set to use this custom Github-MCP-Server in your Claude Desktop**


## 🙌 Acknowledgments
FastMCP by [@jlowin](https://github.com/jlowin)

GitHub REST API v3



## 🤝 Contributing
Contributions are welcome!  
If you have ideas for new GitHub tools, bug fixes, or improvements, feel free to:

1. Open an issue

2. Fork the repo

3. Submit a PR 🚀

## 📫 Contact
For questions or suggestions, reach out via [Twitter](https://x.com/mymadhavyadav07) or raise an issue.
   

   


