import { Layout, Menu, Breadcrumb } from 'antd';
import { UserOutlined, LaptopOutlined, NotificationOutlined } from '@ant-design/icons';
import { Link } from 'react-router-dom'

const { SubMenu } = Menu;
const { Header, Content, Footer, Sider } = Layout;

const CustomLayout = (props) => {
    return (
        <Layout>
            <Header className="header">
                <div className="logo" />
                <Menu theme="dark" mode="horizontal" defaultSelectedKeys={['2']}>
                    <Menu.Item key="1">Example Blog</Menu.Item>
                    <Menu.Item key="2">Posts</Menu.Item>
                </Menu>
            </Header>
            <Content style={{ padding: '0 50px' }}>
                <Breadcrumb style={{ margin: '16px 0' }}>
                    <Breadcrumb.Item><Link to='/'>Home</Link></Breadcrumb.Item>
                    <Breadcrumb.Item><Link to='/'>Posts</Link></Breadcrumb.Item>
                </Breadcrumb>
                <Layout className="site-layout-background" style={{ padding: '24px 0' }}>
                    <Sider className="site-layout-background" width={200}>
                        <Menu
                            mode="inline"
                            defaultSelectedKeys={['1']}
                            defaultOpenKeys={['sub1']}
                            style={{ height: '100%' }}
                        >
                            <SubMenu key="sub1" icon={<UserOutlined />} title="User">
                                <Menu.Item key="1">Register</Menu.Item>
                                <Menu.Item key="2">Login</Menu.Item>
                                <Menu.Item key="3">Logout</Menu.Item>
                            </SubMenu>
                        </Menu>
                    </Sider>
                    <Content style={{ padding: '0 24px', minHeight: 280 }}>
                        {props.children}
                    </Content>
                </Layout>
            </Content>
            <Footer style={{ textAlign: 'center' }}>Copyright &copy; Gray Space It LTD 2020</Footer>
        </Layout>
    );
}

export default CustomLayout;






