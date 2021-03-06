from abidria.serializers import PictureSerializer


class MultipleExperiencesSerializer(object):

    @staticmethod
    def serialize(experiences):
        return [ExperienceSerializer.serialize(experience) for experience in experiences]


class ExperienceSerializer(object):

    @staticmethod
    def serialize(experience):
        return {
                   'id': str(experience.id),
                   'title': experience.title,
                   'description': experience.description,
                   'picture': PictureSerializer.serialize(experience.picture),
               }
