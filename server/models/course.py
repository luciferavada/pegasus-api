from sugar_odm import Model, Field

from . apimodel import APIModel


class Section(Model):
    name = Field(required=True)
    instructor = Field(required=True)
    students = Field(type=[ str ])


class Course(APIModel):

    __rate__ = ( 10, 'secondly' )

    __acl__ = {
        'administrator': ['all'],
        'other': ['read', 'read_all'],
        'unauthorized': ['read', 'read_all']
    }

    name = Field(required=True)
    sections = Field(type=[ Section ])
    description = Field(required=True)
