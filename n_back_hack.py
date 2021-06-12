from PIL import Image
import imagehash


'''
the same path or filename could be an indicator of the same image in the list, however that image could have also been saved as something else, so filenames are not the best indicator here, that's why I have chosen to use random strings for image names to eliminate the option of comparing files name
'''
image_list = ["7575d111f9b557b32100bf4d2b2a010a.png", "9f709058aaf271eb66c4a5dd396e0eb2.png", "cc766966c255c293abda27f05e7bb4a9.png", "4171c558eea6735375f6703a458210a4.png", "03aebfeefda138597ba1947b96a33c9f.png", "04f2a9b323418b86cfa8a9e6e1580bce.png", "70d410468719110ea59d1beb0658138d.png", "90ceec90222930a8e6bc57641eccd60b.png", "af612d38efcca7ff90b2ed5e91a229f2.png", "f2d76ad362df6c5b767921ee5c7ebf42.png", "7ffb444e48d45558c0a556e80b27368b.png", "b7212a022b521ad2991cdb473ba1cb7f.png", "07f5e6d2dec737ea0478f987ca36e0a9.png", "817e95c1d080c0173a79daa4d9a9858d.png", "81bc4b94edd0b4efee8b8ac285414280.png", "639615fec472667818efb859eba74ecc.png", "7e456909fb3da22ee751e2de024fce57.png", "8af3cfdc37616fe49c8053182a2125b5.png", "33556f5c5caf94b55a559054334d1519.png", "1522200ae0bf248a7c3b98cf86d293f5.png", "580e15c43920b20c597cd23e9985b41f.png", "bfb3d152cc1d836e049aa787d76c54a5.png", "8edfa4624928dd6578b3e4d3c92227da.png", "641af62c979dc29d235acd52d1032733.png", "d352ee6a0e7d526d2e8ef9df6ffde8aa.png", "04d2738a375a557a6112867c577e79f9.png", "e7a5af5ea2675cf11f1dc24a54a4cd32.png", "5997552964d1767fc91eee1167b6dbc8.png", "fe6427af21a9095797f73c7f4ab2b3ea.png", "b7718f65a9ff55e7afdf0ddebbcd0f92.png"]

class n_Back_Hack:
    def __init__(self, n_back_num, items=image_list):
        self.n_back_num = n_back_num
        self.items = items

        #number of nbacks found
        self.n_back_count = 0

        self.processing_index = 0
        self.processing_data_type = "queue"

        #set to false of using a data type that is not a path to a file
        self.input_is_image_path = True

        #for queue operation
        self.processing_queue = []

        #for mind like dict
        self.processing_dict = {}

    def hash_image (self, input_image):
        return imagehash.average_hash(Image.open(input_image))

    #no need to use the processing index becasue the queue remains updated
    def update_queue (self, new_item):
        if self.input_is_image_path is True:
            new_item = self.hash_image(new_item)

        if len(self.processing_queue) == self.n_back_num:
            to_compare_against = self.processing_queue.pop(0)
            if to_compare_against == new_item:
                self.n_back_count += 1

        self.processing_queue.append(new_item)

    #not only is the dict way easier for me to process mentally, it is oddly more optimized for computers too, especially for long lists that would be constantly shifting
    def update_dict(self, new_item):
        if self.input_is_image_path is True:
            new_item = self.hash_image(new_item)

        if len(self.processing_dict) == self.n_back_count:
            to_compare_against = self.processing_dict[self.processing_index]

            if to_compare_against == new_item:
                self.n_back_count += 1
            self.processing_dict[self.processing_index] = new_item

            if self.processing_index >= self.n_back_num - 1:
                self.processing_index = 0
            else:
                self.processing_index += 1

    def get_n_back_count(self):

        for item in self.items:
            if self.processing_data_type == "queue":
                self.update_queue(item)
            else:
                self.update_dict(item)

        return self.n_back_count





