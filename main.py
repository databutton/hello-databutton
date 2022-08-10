import databutton as db
import streamlit as st


@db.apps.streamlit(route="/hello", name="Hello Databutton")
def hello():
    st.title("Hello, Databutton")


@db.jobs.repeat_every(seconds=10 * 60)
def repeating_job():
    # Check for new data
    # Do some work on that data
    # Write that data to db.dataframes
    # Send slack notification
    print("Success!")
