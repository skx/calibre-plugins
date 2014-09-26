from calibre.customize import FileTypePlugin

class ResetRating(FileTypePlugin):

    name                    = 'ResetRatings'
    description             = 'When a book is imported set the rating to zero.'
    supported_platforms     = ['windows', 'osx', 'linux']
    author                  = 'Steve Kemp <steve@steve.org.uk>'
    version                 = (0, 0, 2)
    file_types              = set(['epub', 'mobi', 'lit', 'prc', 'azw3'])
    on_postimport           = True

    #
    # We need a very recent version due to previous releases breaking
    # the post-import hook functionality.
    #
    # http://www.mobileread.com/forums/showthread.php?t=246678
    #
    minimum_calibre_version = (2,4,0)

    def run(self, path_to_ebook):
        '''
        NOP
        '''
        return path_to_ebook

    def postimport(self, book_id, book_format, db):
        '''
        Once a book has been added to the database reset the rating field
        '''
        print( "RatingReset::postimport()")
        print( "Current rating: %s" % db.new_api.field_for('rating', book_id))
        db.new_api.set_field('rating', {book_id:0})
