import React from 'react'
import { List, Avatar, Space } from 'antd';
import { MessageOutlined, LikeOutlined, StarOutlined } from '@ant-design/icons';


const IconText = ({ icon, text }) => (
    <Space>
        {React.createElement(icon)}
        {text}
    </Space>
);


const Post = (props) => {
    return (

        <List
            itemLayout="vertical"
            size="large"
            pagination={{
                onChange: page => {
                    console.log(page);
                },
                pageSize: 5,
            }}
            dataSource={props.data}
            renderItem={item => (
                <List.Item
                    key={item.title}
                    actions={[

                    ]}

                >
                    <List.Item.Meta
                        avatar={<Avatar src={item.avatar} />}
                        title={<a href={`${item.id}`}>{item.title}</a>}
                        description={item.body}
                    />
                    {item.content}
                </List.Item>
            )}
        />
    )
}

export default Post;