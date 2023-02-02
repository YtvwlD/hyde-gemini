# TODO: import a library
from .generator import Generator

def serve(site, address, port):
    # TODO: init app
    generator = Generator(site)
    stack = list()
    stack.append(site.content)
    while stack:
        current = stack.pop()
        # TODO
        # app.add_url_rule(
        #     current.url, current.relative_path,
        #     lambda c=current: generator.generate_node(c)
        # )
        for child in current.resources:
            pass  # TODO
            # app.add_url_rule(
            #     child.url, child.relative_path,
            #     lambda c=child: generator.generate_resource(c)
            # )
        for child in current.child_nodes:
            stack.append(child)
    # TODO: app.run(address, port, request_handler=GeminiRequestHandler)
    # TODO: will never be called, probably
    generator.events.site_complete()
    generator.events.generation_complete()
