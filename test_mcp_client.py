from mcp.client.fastmcp import FastMCPClient

# Connect to the MCP server
client = FastMCPClient(
    name="MCP-count-total-rs-client",
    host="127.0.0.1",
    port=5000,
    timeout=10
)

# Call the count_total_rs tool
result = client.call_tool("count_total_rs", text="curry")

print(f"Number of 'r' in 'curry': {result}") 