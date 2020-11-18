import React from 'react'
import axios from 'axios'
import { Card } from 'antd'
import Comments from '../components/Comments'


class PostDetail extends React.Component {

    state = {
        post: {}
    }

    componentDidMount() {
        const postId = this.props.match.params.postId
        axios.get(`https://jsonplaceholder.typicode.com/posts/${postId}`).then(res => {
            this.setState({
                post: res.data
            });
        })

    }
    render() {
        return (
            <div>
                <Card title={this.state.post.title}>
                    <p>{this.state.post.body}</p>
                </Card>
                <h1>Comment Section</h1>
                <Comments />
            </div>
        )
    }
}

export default PostDetail;