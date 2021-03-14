//import {gql} from 'graphql-tag';
const {ApolloServer, PubSub} = require('apollo-server');
const mongoose = require('mongoose');
const {MONGODB} = require('./config');
const resolvers = require('./graphql/resolvers');
const typeDefs = require('./graphql/typeDefs');
const pubsub = new PubSub();
const PORT = process.env.port || 5000;

const server = new ApolloServer({
    typeDefs,
    resolvers,
    context:({req}) => ({req, pubsub})
})

mongoose.connect( MONGODB,{ useNewUrlParser: true} )
.then(() => {
    console.log('MongoDB Connected');
    return server.listen({ port: PORT});
})
.then(res => {
    console.log(`server รันอยู่จร้า`);
})
.catch(err => {
    console.error(err)
})