import asyncio
from gql import Client, gql
from gql.transport.aiohttp import AIOHTTPTransport

async def main():
    # Set transport ke endpoint server GraphQL
    transport = AIOHTTPTransport(url="http://localhost:8000/graphql")
    client = Client(transport=transport)
    
    # Query GraphQL untuk mengambil semua kolom data buku
    query = gql(
        """
        query getSemuaBuku {
          semuaBuku {
            id
            kodeRak
            judul
            harga
            apakahTersedia
          }
        }
        """
    )
    
    async with client as session:
        result = await session.execute(query)
        print("--- HASIL QUERY GRAPHQL TOKO BUKU ---")
        print(result)

asyncio.run(main())