from typing import List

from PIL import Image
from pydantic import BaseModel


class Modality:
    """A Base Class for Modality Types"""

    TEXT = "TEXT"
    IMAGE = "IMAGE"
    PDF = "PDF"
    MP4 = "MP4"


class ScrubbingProvider(BaseModel):
    """A Base Class for Scrubbing Providers"""

    name: str
    capabilities: List[str]

    class Config:
        arbitrary_types_allowed = True

    def scrub_text(self, text: str, is_separated: bool = False) -> str:
        raise NotImplementedError

    def scrub_image(
        self, image: Image, fill_color: int = config.SCRUB_FILL_COLOR
    ) -> Image:
        raise NotImplementedError

    def scrub_pdf(self):
        raise NotImplementedError

    def scrub_mp4(self):
        raise NotImplementedError
