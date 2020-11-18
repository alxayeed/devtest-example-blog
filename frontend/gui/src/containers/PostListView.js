import React from 'react'
import Post from '../components/Post';
import axios from 'axios'

class PostList extends React.Component {

    state = {
        posts: []
    }

    componentDidMount() {
        axios.get('https://jsonplaceholder.typicode.com/posts/').then(res => {
            this.setState({
                posts: res.data
            });
            console.log(res.data)
        })

    }
    render() {
        return (
            <Post data={this.state.posts} />
        )
    }
}

export default PostList;