from enum import Enum


class PollStatus(Enum):
    DRAFT = 'draft'
    PUBLISHED = 'published'
    ENDED = 'ended'