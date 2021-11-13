import asyncio

async def say(string_to_print:str, time_to_sleep:int):
    await asyncio.sleep(time_to_sleep)
    print(string_to_print)
    
async def sequence_saying():
    await say('hello', 2)
    await say('world', 3)
    print("starting...")
    
    
async def main():
    await sequence_saying()
    await asyncio.gather(
        say("Will be the last print", 3),
        say("Will be the second print", 2),
        say("Will be the first print", 1),
    )
asyncio.run(main())

# expected output:
# hello
# world
# starting...
# Will be the first print
# Will be the second print
# Will be the last print


