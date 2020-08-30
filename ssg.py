import typer
import site from ssg.site

def main(source = "content", dest = "dist"):
    config = {"source":source, "dest" : dest}
    s = site(source, dest, **)
    s.build()

tyoer.run(main)