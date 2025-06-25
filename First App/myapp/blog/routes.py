from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from myapp.models import db, BlogPost

blog = Blueprint('blog', __name__, template_folder='templates/blog')

@blog.route('/myblogs')
@login_required
def my_blogs():
    blogs = BlogPost.query.filter_by(author=current_user).all()
    return render_template('my_blogs.html', blogs=blogs)


@blog.route('/create', methods=['GET', 'POST'])
@login_required
def create_blog():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        is_public = 'is_public' in request.form  # checkbox presence

        new_blog = BlogPost(
            title=title,
            content=content,
            is_public=is_public,
            author=current_user
        )

        db.session.add(new_blog)
        db.session.commit()

        flash('Blog post created!', 'success')
        return redirect(url_for('blog.my_blogs'))

    return render_template('create_blog.html')


@blog.route('/delete/<int:blog_id>')
@login_required
def delete_blog(blog_id):
    blog = BlogPost.query.get_or_404(blog_id)

    if blog.author != current_user:
        flash("You can't delete another user's blog.", 'error')
        return redirect(url_for('blog.my_blogs'))

    db.session.delete(blog)
    db.session.commit()

    flash('Blog deleted successfully.', 'success')
    return redirect(url_for('blog.my_blogs'))


@blog.route('/toggle-public/<int:blog_id>')
@login_required
def toggle_public(blog_id):
    blog = BlogPost.query.get_or_404(blog_id)

    if blog.author != current_user:
        flash("You can't modify another user's blog.", 'error')
        return redirect(url_for('blog.my_blogs'))

    # Toggle public/private
    blog.is_public = not blog.is_public
    db.session.commit()

    flash('Blog visibility updated.', 'success')
    return redirect(url_for('blog.my_blogs'))


@blog.route('/blog/<int:blog_id>')
def blog_detail(blog_id):
    blog = BlogPost.query.get_or_404(blog_id)

    # Only allow owner or public blogs to be viewed
    if not blog.is_public and (not current_user.is_authenticated or blog.author != current_user):
        flash("This blog is private.", "error")
        return redirect(url_for("home.index"))

    return render_template("blog_detail.html", blog=blog)