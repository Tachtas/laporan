import streamlit as st
import asyncio
from utils.db_connector import get_data

async def main():
    # Get data section
    st.header("Feed from Media Table")
    data = await get_data()
    data = data[0]['result']
    st.write(data)


if __name__ == "__main__":
    asyncio.run(main())