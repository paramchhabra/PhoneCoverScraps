import requests
from bs4 import BeautifulSoup
from rich import print
import re
import json
import os
from db_stat import *
import asyncio
from sites import *

async def main():
    print("Main")
    await mainfunc()
    await get_data()

if __name__=="__main__":
    asyncio.run(main())

