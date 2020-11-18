import React from 'react'
import { Route } from 'react-router-dom'
import PostDetail from './containers/PostDetailView';
import PostList from './containers/PostListView';

const BaseRouter = () => {
    return (
        <div>
            <Route exact path='/' component={PostList} />
            <Route exact path='/:postId' component={PostDetail} />
        </div>
    )
}

export default BaseRouter;