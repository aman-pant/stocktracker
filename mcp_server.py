from mcp.server.fastmcp import FastMCP

# FastMCP is a fast implementation of the MCP protocol
# It is designed to be used with the MCP server

#create a MCP server
mcp = FastMCP("MCP-count-total-rs",
              host="127.0.0.1",
              port=5000,
              timeout=30)

@mcp.tool()
def count_total_rs(text: str) -> int:
    """
    Count the total number of records in the specified text.

    Args:
        text (str): The text to count of Rs.

    Returns:
        int: The total number of Rs in the text.
    """
    # Simulate counting records in a table
    # In a real implementation, this would query the database
    if not isinstance(text, str):
        raise ValueError("Input must be a string")

    return text.lower().count("r")

if __name__ == "__main__":
    # Start the MCP server
    mcp.run()