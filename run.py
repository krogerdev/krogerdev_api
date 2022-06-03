from app import createapp

app = createapp()

@app.errorhandler(404)
def not_found(e):
    return {
        "error": "404 resource not found"
    }


if __name__ == '__main__':
    app.run()
