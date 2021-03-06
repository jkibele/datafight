Title: Getting this Blog Working with IPython Notebook
Date: 2013-09-19 10:23
Category: Python
Tags: pelican, publishing, ipython notebook
Slug: getting-this-blog-working
Author: Jared Kibele
Summary: I wanted to post some IPython stuff on a blog and found it rather difficult on [Blogger](http://datafight.blogspot.com) so I started digging around for an alternative. From what I can tell, static blog generators are the way to go for this sort of thing if you're geek enough to deal with the setup and ongoing operation. This is how I did it...

I'm using IPython Notebook 1.1.0. in my work. I wanted to post some IPython stuff on a blog and found it rather difficult to do so on Blogger so I started digging around for an alternative. From what I can tell, static blog generators are the way to go for this sort of thing if you're geek enough to deal with the setup and ongoing operation. It's not as simple as Wordpress or Blogger but shouldn't be too bad if you're comfortable with Python and GitHub and whatnot. Basically, I decided that I'm geek enough.

I started out following the directions I found [here](http://themodernscientist.com/posts/2013/2013-06-02-my_octopelican_python_blog/). However, this stuff changes pretty fast and it seems like things are a bit different now. The changes specified [here](https://github.com/modernscientist/modernscientist.github.com/blob/master/notes/importing_ipython_notebooks_in_a_pelican_blog.md) are no longer needed. I installed pelican using the development version cloned from GitHub. The version installed by pip didn't work with the GitHub version of liquid tags. It took me a while to figure that out. Hopefully I can save someone else some time or at least save myself some time when I go to replicate this on my laptop.

So, assuming you've got ipython 1.1.0 already, I guess the proceedure is:

1. Get pelican by doing `git clone https://github.com/getpelican/pelican.git`, then going to where pelican was cloned (`cd pelican`) and typing `python setup.py install`. Use `sudo python setup.py install` if you have permission problems.

2. I'm using the Octopress template. To use that, go [clone it from GitHub](https://github.com/duilio/pelican-octopress-theme). Then do `sudo pelican-themes -i /path/to/pelican-octopress-theme/`.

3. Go clone [pelican-plugins](https://github.com/getpelican/pelican-plugins) and follow the directions in the [liquid tags readme](https://github.com/getpelican/pelican-plugins/tree/master/liquid_tags).
