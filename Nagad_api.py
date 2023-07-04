from fastapi import FastAPI
from pydantic import BaseModel
import asyncio
from typing import List, Union
import uvicorn
from Nagad_AI import *




app = FastAPI()

class Item(BaseModel):
    url: str

async def process_item(item: Item):
    result = await mainDetect(item.url)
    result = json.loads(result)
    return result

async def process_items(items: Union[Item, List[Item]]):
    if isinstance(items, list):
        coroutines = [process_item(item) for item in items]
        results_dict = await asyncio.gather(*coroutines)
        results = {}
        for item in results_dict:
            results.update(item)


    else:
        results = await process_item(items)
    return results
 
@app.post("/nagad")
async def create_items(items: Union[Item, List[Item]]):
    results = await process_items(items)
    print("Result Sent to User:", results)
    print("###################################################################################################")
    print("Last Execution Time : ", time())
    return results


# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8020)
