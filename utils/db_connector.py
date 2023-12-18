from surrealdb import Surreal
import streamlit as st

# Function to fetch data from the "media" table
async def get_data():
    async with Surreal(st.secrets["URL"]) as db:
        await db.signin({"user": st.secrets["USER"], "pass": st.secrets["PASS"]})
        await db.use(st.secrets["DB"],st.secrets["NS"])

        result = await db.query("select * from salesman")
        #data = result["data"]

        return result