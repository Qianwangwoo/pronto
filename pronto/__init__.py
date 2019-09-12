__author__ = "Martin Larralde <martin.larralde@embl.de>"
__license__ = "MIT"
__version__ = (
    __import__('pkg_resources')
    .resource_string(__name__, "_version.txt")
    .decode('utf-8')
    .strip()
)

from .ontology import Ontology  # noqa: F401
from .term import Term  # noqa: F401
from .definition import Definition  # noqa: F401
from .relationship import Relationship  # noqa: F401
from .synonym import Synonym, SynonymType  # noqa: F401
from .xref import Xref  # noqa: F401
